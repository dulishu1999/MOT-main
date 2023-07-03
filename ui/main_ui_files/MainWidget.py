import os.path
import subprocess
import sys
import threading
from PySide6 import QtWidgets, QtCore
from ui.main_ui_files import GeneralUI, OptimizerUI, NetworkUI, SavingUI, BucketUI, NoiseOffsetUI, SampleUI, LoggingUI, \
    SubDatasetUI, QueueWidget
from ui.modules import TomlFunctions, validator


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super(MainWidget, self).__init__(parent)
        self.main_layout = QtWidgets.QGridLayout()#生成一个主布局
        self.setLayout(self.main_layout)#将主布局加到self

        self.args_widget = ArgsWidget()#生成一个模型参数部件的对象
        self.subset_widget = SubDatasetUI.SubDatasetWidget()#生成一个子数据集部件对象
        self.subset_widget.add_empty_subset("subset 1")#添加一个空的子数据集，这样在界面上，初始的时候会有一个空的子数据集部件

        self.args = {}#模型初始参数为空
        self.dataset_args = {}#数据集初始参数为空
        self.training_thread = None#初始训练的线程也指向none

        self.middle_divider = QtWidgets.QFrame()#中间分隔frame
        self.middle_divider.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.middle_divider.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.queue_widget = QueueWidget.QueueWidget()#队列部件
        self.queue_widget.saveQueue.connect(self.save_toml)
        self.queue_widget.loadQueue.connect(self.load_toml)
        self.begin_training_button = QtWidgets.QPushButton("Start Training")#开始训练的按键
        self.begin_training_button.setSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum,
                                                 QtWidgets.QSizePolicy.Policy.Minimum)

        self.main_layout.addWidget(self.args_widget, 0, 0, 1, 1)#模型参数部件
        self.main_layout.addWidget(self.middle_divider, 0, 1, 1, 1)#中间分隔的部件
        self.main_layout.addWidget(self.subset_widget, 0, 2, 1, 1)#子数据集部件
        self.main_layout.addWidget(self.queue_widget, 1, 0, 1, 2)#队列部件
        self.main_layout.addWidget(self.begin_training_button, 1, 2, 1, 1)#开始训练的按钮
        self.main_layout.setColumnStretch(0, 1)
        self.main_layout.setColumnStretch(2, 1)

        self.begin_training_button.clicked.connect(self.begin_train)#训练按键连接开始训练的槽函数
        self.args_widget.general_args.CacheLatentsChecked.connect(self.subset_widget.cache_checked)

    @QtCore.Slot()
    def begin_train(self) -> None:
        if self.training_thread and self.training_thread.is_alive():#如果训练的线程是启动的，点击开始训练的button是无效的
            return
        self.training_thread = threading.Thread(target=self.train_thread)#启动一个线程，这个线程执行的目标函数是train_thread
        self.training_thread.start()#启动线程

    def validate_args(self) -> bool:
        args, dataset_args = self.args_widget.collate_args()#参数整理后返回基础参数和数据集参数，点击
        dataset_args['subsets'] = self.subset_widget.get_subset_args()#获取子数据集参数
        self.training_thread = threading.Thread(target=self.train_thread)
        args = validator.validate_args(args)
        dataset_args = validator.validate_dataset_args(dataset_args)
        if not args or not dataset_args:
            print("failed validation")
            return False
        validator.validate_restarts(args, dataset_args)
        validator.validate_warmup_ratio(args, dataset_args)
        validator.validate_save_tags(args, dataset_args)
        if "save_toml" in args:
            del args['save_toml']
            TomlFunctions.save_toml(self.save_args(), os.path.join(args['output_dir'],
                                                                   f"auto_save_{args.get('output_name', 'last')}.toml"))
        self.create_config_args_file(args)
        self.create_dataset_args_file(dataset_args)
        print("validated, starting training...")
        return True
    #训练的线程
    def train_thread(self):
        self.begin_training_button.setEnabled(False)#将开始训练的button置为false
        python = sys.executable#该属性是一个字符串，在正常情况下，其值是当前运行的 Python 解释器对应的可执行程序所在的绝对路径。
        if len(self.queue_widget.elements) == 0:
            if not self.validate_args():#如果参数验证没有通过
                self.begin_training_button.setEnabled(True)
                return
            try:
                subprocess.check_call([python, os.path.join("ui","sd_scripts", "train_network.py"),
                                       f"--config_file={os.path.join('ui','runtime_store', 'config.toml')}",
                                       f"--dataset_config={os.path.join('ui','runtime_store', 'dataset.toml')}"])
            except subprocess.SubprocessError as e:
                print(f"Failed to train because of error:\n{e}")
            files = [os.path.join("ui","runtime_store", "config.toml"), os.path.join("ui","runtime_store", "dataset.toml")]
            for file in files:
                try:
                    os.remove(file)
                except FileNotFoundError:
                    pass
            self.begin_training_button.setEnabled(True)
            return
        while len(self.queue_widget.elements) > 0:#看样子是根据队列中的项目数，多少个项目执行多少次训练指令
            try:
                file = os.path.join("ui","runtime_store", f"{self.queue_widget.elements[0].queue_file}.toml")#读取批量的toml文件
                self.queue_widget.remove_first_from_queue()
                base_args = TomlFunctions.load_toml(file)
                args, dataset_args = validator.separate_and_validate(base_args)
                if not args or not dataset_args:
                    print("some args are not valid, skipping.")#如果缺少数据集参数或者模型参数，就会跳过改项目模型的训练
                    continue
                validator.validate_restarts(args, dataset_args)
                validator.validate_warmup_ratio(args, dataset_args)
                validator.validate_save_tags(args, dataset_args)
                if "save_toml" in args:#
                    del args['save_toml']
                    TomlFunctions.save_toml(base_args, os.path.join(args['output_dir'],
                                                                    f"auto_save_{args.get('output_name', 'last')}.toml"))
                self.create_config_args_file(args)#创造一个参数配置文件
                self.create_dataset_args_file(dataset_args)#创建一个数据集参数配置文件
                print("validated, starting training...")#参数验证通过开始训练
                subprocess.check_call([python, os.path.join("ui","sd_scripts", "train_network.py"),
                                       f"--config_file={os.path.join('ui','runtime_store', 'config.toml')}",
                                       f"--dataset_config={os.path.join('ui','runtime_store', 'dataset.toml')}"])#这相当于就是执行一个带参的训练指令
            except BaseException as e:
                if not isinstance(e, subprocess.SubprocessError):
                    print(f"Failed to train because of error:\n{e}")
        for file in os.listdir("runtime_store"):
            if file != '.gitignore':
                os.remove(os.path.join("ui","runtime_store", file))
        self.begin_training_button.setEnabled(True)

    def save_args(self) -> dict:
        args = self.args_widget.save_args()
        args['subsets'] = self.subset_widget.get_subset_args(skip_check=True)
        return args

    def load_args(self, args: dict) -> None:
        self.args_widget.load_args(args)
        self.subset_widget.load_args(args)

    @QtCore.Slot(str)
    def save_toml(self, file_name: str = None) -> None:
        args = self.save_args()
        if file_name:
            TomlFunctions.save_toml(args, os.path.join("ui","runtime_store", f"{file_name}.toml"))
        else:
            TomlFunctions.save_toml(args)

    @QtCore.Slot(str)
    def load_toml(self, file_name: str = None) -> None:
        if file_name:
            args = TomlFunctions.load_toml(os.path.join("ui","runtime_store", f"{file_name}.toml"))
        else:
            args = TomlFunctions.load_toml()
        if not args:
            return
        self.load_args(args)

    @staticmethod
    def create_config_args_file(args: dict) -> None:
        with open(os.path.join("ui","runtime_store", "config.toml"), 'w') as f:
            for key, value in args.items():
                if isinstance(value, str):
                    value = f"\'{value}\'"
                if isinstance(value, bool):
                    value = f"{value}".lower()
                f.write(f"{key} = {value}\n")

    @staticmethod
    def create_dataset_args_file(args: dict) -> None:
        with open(os.path.join("ui","runtime_store", "dataset.toml"), 'w') as f:
            f.write("[general]\n")
            for key, value in args['general'].items():
                if isinstance(value, str):
                    value = f"\'{value}\'"
                if isinstance(value, bool):
                    value = f"{value}".lower()
                f.write(f"{key} = {value}\n")
            f.write("\n[[datasets]]\n")
            for subset in args['subsets']:
                f.write("\n\t[[datasets.subsets]]\n")
                for key, value in subset.items():
                    if isinstance(value, str):
                        value = f"\'{value}\'"
                    if isinstance(value, bool):
                        value = f"{value}".lower()
                    f.write(f"\t{key} = {value}\n")


class ArgsWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super(ArgsWidget, self).__init__(parent)
        # setup default values
        self.setMinimumSize(600, 300)
        self.setLayout(QtWidgets.QVBoxLayout())

        # setup scroll area for the widget
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_area.setWidget(self.scroll_widget)
        self.layout().addWidget(self.scroll_area)

        # setup layout stuff for scroll_widget
        self.scroll_widget.setLayout(QtWidgets.QVBoxLayout())
        self.scroll_widget.layout().setSpacing(0)
        self.scroll_widget.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.scroll_widget.layout().setContentsMargins(0, 0, 0, 0)

        self.args_widget_array = []

        # add base_args
        self.general_args = GeneralUI.BaseArgsWidget()
        self.general_args.colap.toggle_collapsed()
        self.general_args.colap.title_frame.setChecked(True)
        self.args_widget_array.append(self.general_args)#args_widget_array是参数部件列表，并将general_args部件实例对象加入这个列表中

        # add the rest of the args widgets
        self.network_args = NetworkUI.NetworkWidget()
        self.args_widget_array.append(self.network_args)#添加
        self.optimizer_args = OptimizerUI.OptimizerWidget()
        self.args_widget_array.append(self.optimizer_args)#添加
        self.saving_args = SavingUI.SavingWidget()
        self.args_widget_array.append(self.saving_args)#添加
        self.bucket_args = BucketUI.BucketWidget()
        self.args_widget_array.append(self.bucket_args)#添加
        self.noise_args = NoiseOffsetUI.NoiseOffsetWidget()
        self.args_widget_array.append(self.noise_args)#添加
        self.sample_args = SampleUI.SampleWidget()
        self.args_widget_array.append(self.sample_args)#添加
        self.logging_args = LoggingUI.LoggingWidget()
        self.args_widget_array.append(self.logging_args)#添加

        # set all args widgets into layout 将所有的部件添加到布局中
        for widget in self.args_widget_array:
            self.scroll_widget.layout().addWidget(widget)
    #参数的整理  参数有两个，一个是args，一个是dataset_args
    def collate_args(self) -> tuple[dict, dict]:
        args = {}
        dataset_args = {}
        for widget in self.args_widget_array:
            widget.get_args(args)#按引用传递
            widget.get_dataset_args(dataset_args)
        return args, dataset_args
    #参数的保存
    def save_args(self) -> dict:
        args = {}
        for widget in self.args_widget_array:#遍历参数项列表
            widget_args = widget.save_args()
            widget_dataset_args = widget.save_dataset_args()
            args[widget.name] = {}
            if widget_args:
                args[widget.name]['args'] = widget_args.copy()
            if widget_dataset_args:
                args[widget.name]['dataset_args'] = widget_dataset_args.copy()
        return args
    #参数的导入
    def load_args(self, args: dict) -> None:
        for widget in self.args_widget_array:
            if hasattr(widget, "load_args"):
                widget.load_args(args)
