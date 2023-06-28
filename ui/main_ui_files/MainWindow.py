import json
import os
from PySide6 import QtWidgets, QtGui, QtCore
from qt_material import QtStyleTools, apply_stylesheet
from ui.main_ui_files.MainWidget import MainWidget
from ui.ui_files.MainUI import Ui_MainWindow


class TrainMainWindow(QtWidgets.QMainWindow, QtStyleTools):
    def __init__(self, app: QtWidgets.QApplication = None):
        super(TrainMainWindow, self).__init__()
        self.app = app
        self.window_ = Ui_MainWindow()
        self.window_.setupUi(self)
        self.setMinimumSize(1450, 725)
        self.main_widget = MainWidget()
        self.setCentralWidget(self.main_widget)

        # setup theme actions for menu bar
        self.dark_themes, self.light_themes = self.process_themes()
        for theme in self.dark_themes:
            self.window_.dark_theme_menu.addAction(theme)
        for theme in self.light_themes:
            self.window_.light_theme_menu.addAction(theme)

        # setup theme switching
        for i in range(len(self.dark_themes)):
            self.dark_themes[i].triggered.connect(lambda x=False, index=i: self.change_theme(index, False))
        for i in range(len(self.light_themes)):
            self.light_themes[i].triggered.connect(lambda x=False, index=i: self.change_theme(index, True))

        # setup TOML saving and loading actions
        self.window_.save_toml.triggered.connect(self.main_widget.save_toml)
        self.window_.load_toml.triggered.connect(self.main_widget.load_toml)
    #UI主题风格处理
    def process_themes(self) -> tuple[list, list]:
        themes = os.listdir(os.path.join("ui","css", "themes"))
        dark_themes = []
        light_themes = []
        for theme in themes:
            is_dark = len(theme.split("dark")) > 1
            if len(theme.split("500")) > 1:
                continue
            if is_dark:
                dark_themes.append(QtGui.QAction(theme.split("_")[1].replace(".xml", ""), self))
            else:
                light_themes.append(QtGui.QAction(theme.split("_")[1].replace(".xml", ""), self))
        return dark_themes, light_themes

    @QtCore.Slot(int, bool)
    def change_theme(self, theme_index: int, is_light: bool) -> None:
        prefix = "light" if is_light else "dark"
        name = self.dark_themes[theme_index].text() if not is_light else self.light_themes[theme_index].text()
        apply_stylesheet(self.app, theme=os.path.join("ui","css", "themes", f"{prefix}_{name}.xml"),
                         invert_secondary=is_light)
        if os.path.exists("config.json"):
            with open("config.json", 'r') as f:
                config = json.load(f)
            config['theme'] = {
                'location': os.path.join("ui","css", "themes", f"{prefix}_{name}.xml"),
                'is_light': is_light
            }
            with open("config.json", 'w') as f:
                json.dump(config, f, indent=4)
        else:
            with open("config.json", 'w') as f:
                config = {"theme": {
                    "location": os.path.join("ui","css", "themes", f"{prefix}_{name}.xml"),
                    "is_light": is_light
                }}
                json.dump(config, f, indent=4)
