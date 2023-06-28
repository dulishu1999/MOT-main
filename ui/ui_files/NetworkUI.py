# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NetworkUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QLabel, QScrollArea, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

from ui.modules.CollapsibleWidget import CollapsibleWidget
from ui.modules.ScrollOnSelect import (ComboBox, DoubleSpinBox, SpinBox, TabView)

class Ui_network_ui(object):
    def setupUi(self, network_ui):
        if not network_ui.objectName():
            network_ui.setObjectName(u"network_ui")
        network_ui.resize(443, 260)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(network_ui.sizePolicy().hasHeightForWidth())
        network_ui.setSizePolicy(sizePolicy)
        network_ui.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(network_ui)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = TabView(network_ui)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        self.main_tab.setFocusPolicy(Qt.NoFocus)
        self.gridLayout = QGridLayout(self.main_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.algo_select = ComboBox(self.main_tab)
        self.algo_select.addItem("")
        self.algo_select.addItem("")
        self.algo_select.addItem("")
        self.algo_select.addItem("")
        self.algo_select.addItem("")
        self.algo_select.addItem("")
        self.algo_select.addItem("")
        self.algo_select.setObjectName(u"algo_select")
        self.algo_select.setFocusPolicy(Qt.StrongFocus)

        self.gridLayout.addWidget(self.algo_select, 0, 0, 1, 2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.network_dim_label = QLabel(self.main_tab)
        self.network_dim_label.setObjectName(u"network_dim_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.network_dim_label)

        self.network_dim_input = SpinBox(self.main_tab)
        self.network_dim_input.setObjectName(u"network_dim_input")
        self.network_dim_input.setMaximumSize(QSize(16777215, 16777215))
        self.network_dim_input.setFocusPolicy(Qt.StrongFocus)
        self.network_dim_input.setMinimum(1)
        self.network_dim_input.setMaximum(16777215)
        self.network_dim_input.setValue(32)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.network_dim_input)

        self.network_alpha_label = QLabel(self.main_tab)
        self.network_alpha_label.setObjectName(u"network_alpha_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.network_alpha_label)

        self.network_alpha_input = DoubleSpinBox(self.main_tab)
        self.network_alpha_input.setObjectName(u"network_alpha_input")
        self.network_alpha_input.setMaximumSize(QSize(16777215, 16777215))
        self.network_alpha_input.setFocusPolicy(Qt.StrongFocus)
        self.network_alpha_input.setDecimals(2)
        self.network_alpha_input.setMaximum(16777215.000000000000000)
        self.network_alpha_input.setValue(16.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.network_alpha_input)


        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.conv_dim_label = QLabel(self.main_tab)
        self.conv_dim_label.setObjectName(u"conv_dim_label")
        self.conv_dim_label.setEnabled(True)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.conv_dim_label)

        self.conv_dim_input = SpinBox(self.main_tab)
        self.conv_dim_input.setObjectName(u"conv_dim_input")
        self.conv_dim_input.setEnabled(False)
        self.conv_dim_input.setFocusPolicy(Qt.StrongFocus)
        self.conv_dim_input.setMaximum(16777215)
        self.conv_dim_input.setValue(32)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.conv_dim_input)

        self.conv_alpha_label = QLabel(self.main_tab)
        self.conv_alpha_label.setObjectName(u"conv_alpha_label")
        self.conv_alpha_label.setEnabled(True)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.conv_alpha_label)

        self.conv_alpha_input = DoubleSpinBox(self.main_tab)
        self.conv_alpha_input.setObjectName(u"conv_alpha_input")
        self.conv_alpha_input.setEnabled(False)
        self.conv_alpha_input.setFocusPolicy(Qt.StrongFocus)
        self.conv_alpha_input.setMaximum(16777215.000000000000000)
        self.conv_alpha_input.setValue(16.000000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.conv_alpha_input)


        self.gridLayout.addLayout(self.formLayout_2, 1, 1, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.dylora_unit_label = QLabel(self.main_tab)
        self.dylora_unit_label.setObjectName(u"dylora_unit_label")
        self.dylora_unit_label.setEnabled(True)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.dylora_unit_label)

        self.dylora_unit_input = SpinBox(self.main_tab)
        self.dylora_unit_input.setObjectName(u"dylora_unit_input")
        self.dylora_unit_input.setEnabled(False)
        self.dylora_unit_input.setMaximumSize(QSize(16777215, 16777215))
        self.dylora_unit_input.setFocusPolicy(Qt.StrongFocus)
        self.dylora_unit_input.setValue(4)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.dylora_unit_input)

        self.lyco_dropout_enable = QCheckBox(self.main_tab)
        self.lyco_dropout_enable.setObjectName(u"lyco_dropout_enable")
        self.lyco_dropout_enable.setEnabled(False)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lyco_dropout_enable)

        self.lyco_dropout_input = DoubleSpinBox(self.main_tab)
        self.lyco_dropout_input.setObjectName(u"lyco_dropout_input")
        self.lyco_dropout_input.setEnabled(False)
        self.lyco_dropout_input.setMaximumSize(QSize(16777215, 16777215))
        self.lyco_dropout_input.setFocusPolicy(Qt.StrongFocus)
        self.lyco_dropout_input.setMaximum(1.000000000000000)
        self.lyco_dropout_input.setSingleStep(0.010000000000000)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lyco_dropout_input)

        self.cp_enable = QCheckBox(self.main_tab)
        self.cp_enable.setObjectName(u"cp_enable")
        self.cp_enable.setEnabled(False)

        self.formLayout_3.setWidget(3, QFormLayout.SpanningRole, self.cp_enable)

        self.unet_te_both_label = QLabel(self.main_tab)
        self.unet_te_both_label.setObjectName(u"unet_te_both_label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.unet_te_both_label)

        self.unet_te_both_select = ComboBox(self.main_tab)
        self.unet_te_both_select.addItem("")
        self.unet_te_both_select.addItem("")
        self.unet_te_both_select.addItem("")
        self.unet_te_both_select.setObjectName(u"unet_te_both_select")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.unet_te_both_select.sizePolicy().hasHeightForWidth())
        self.unet_te_both_select.setSizePolicy(sizePolicy1)
        self.unet_te_both_select.setMinimumSize(QSize(0, 0))
        self.unet_te_both_select.setMaximumSize(QSize(16777215, 16777215))
        self.unet_te_both_select.setFocusPolicy(Qt.StrongFocus)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.unet_te_both_select)


        self.gridLayout.addLayout(self.formLayout_3, 2, 0, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.network_dropout_enable = QCheckBox(self.main_tab)
        self.network_dropout_enable.setObjectName(u"network_dropout_enable")
        self.network_dropout_enable.setEnabled(True)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.network_dropout_enable)

        self.network_dropout_input = DoubleSpinBox(self.main_tab)
        self.network_dropout_input.setObjectName(u"network_dropout_input")
        self.network_dropout_input.setEnabled(False)
        self.network_dropout_input.setFocusPolicy(Qt.StrongFocus)
        self.network_dropout_input.setMaximum(1.000000000000000)
        self.network_dropout_input.setSingleStep(0.010000000000000)
        self.network_dropout_input.setValue(0.100000000000000)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.network_dropout_input)

        self.rank_dropout_enable = QCheckBox(self.main_tab)
        self.rank_dropout_enable.setObjectName(u"rank_dropout_enable")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.rank_dropout_enable)

        self.rank_dropout_input = DoubleSpinBox(self.main_tab)
        self.rank_dropout_input.setObjectName(u"rank_dropout_input")
        self.rank_dropout_input.setEnabled(False)
        self.rank_dropout_input.setFocusPolicy(Qt.StrongFocus)
        self.rank_dropout_input.setMaximum(1.000000000000000)
        self.rank_dropout_input.setSingleStep(0.010000000000000)
        self.rank_dropout_input.setValue(0.100000000000000)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.rank_dropout_input)

        self.module_dropout_enable = QCheckBox(self.main_tab)
        self.module_dropout_enable.setObjectName(u"module_dropout_enable")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.module_dropout_enable)

        self.module_dropout_input = DoubleSpinBox(self.main_tab)
        self.module_dropout_input.setObjectName(u"module_dropout_input")
        self.module_dropout_input.setEnabled(False)
        self.module_dropout_input.setFocusPolicy(Qt.StrongFocus)
        self.module_dropout_input.setMaximum(1.000000000000000)
        self.module_dropout_input.setSingleStep(0.010000000000000)
        self.module_dropout_input.setValue(0.100000000000000)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.module_dropout_input)


        self.gridLayout.addLayout(self.formLayout_4, 2, 1, 1, 1)

        self.tabWidget.addTab(self.main_tab, "")
        self.block_weight_tab = QWidget()
        self.block_weight_tab.setObjectName(u"block_weight_tab")
        self.block_weight_tab.setFocusPolicy(Qt.NoFocus)
        self.verticalLayout_2 = QVBoxLayout(self.block_weight_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.block_weight_scroll_area = QScrollArea(self.block_weight_tab)
        self.block_weight_scroll_area.setObjectName(u"block_weight_scroll_area")
        self.block_weight_scroll_area.setWidgetResizable(True)
        self.block_weight_scroll_widget = QWidget()
        self.block_weight_scroll_widget.setObjectName(u"block_weight_scroll_widget")
        self.block_weight_scroll_widget.setGeometry(QRect(0, 0, 437, 228))
        self.verticalLayout_3 = QVBoxLayout(self.block_weight_scroll_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.block_weight_widget = CollapsibleWidget(self.block_weight_scroll_widget)
        self.block_weight_widget.setObjectName(u"block_weight_widget")
        self.block_weight_widget.setEnabled(True)

        self.verticalLayout_3.addWidget(self.block_weight_widget)

        self.dim_block_widget = CollapsibleWidget(self.block_weight_scroll_widget)
        self.dim_block_widget.setObjectName(u"dim_block_widget")
        self.dim_block_widget.setEnabled(True)

        self.verticalLayout_3.addWidget(self.dim_block_widget)

        self.alpha_block_widget = CollapsibleWidget(self.block_weight_scroll_widget)
        self.alpha_block_widget.setObjectName(u"alpha_block_widget")
        self.alpha_block_widget.setEnabled(True)

        self.verticalLayout_3.addWidget(self.alpha_block_widget)

        self.conv_block_widget = CollapsibleWidget(self.block_weight_scroll_widget)
        self.conv_block_widget.setObjectName(u"conv_block_widget")
        self.conv_block_widget.setEnabled(False)

        self.verticalLayout_3.addWidget(self.conv_block_widget)

        self.conv_alpha_block_widget = CollapsibleWidget(self.block_weight_scroll_widget)
        self.conv_alpha_block_widget.setObjectName(u"conv_alpha_block_widget")
        self.conv_alpha_block_widget.setEnabled(False)

        self.verticalLayout_3.addWidget(self.conv_alpha_block_widget)

        self.block_weight_scroll_area.setWidget(self.block_weight_scroll_widget)

        self.verticalLayout_2.addWidget(self.block_weight_scroll_area)

        self.tabWidget.addTab(self.block_weight_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(network_ui)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(network_ui)
    # setupUi

    def retranslateUi(self, network_ui):
        network_ui.setWindowTitle(QCoreApplication.translate("network_ui", u"Form", None))
        self.algo_select.setItemText(0, QCoreApplication.translate("network_ui", u"LoRA", None))
        self.algo_select.setItemText(1, QCoreApplication.translate("network_ui", u"LoCon", None))
        self.algo_select.setItemText(2, QCoreApplication.translate("network_ui", u"LoCon (LyCORIS)", None))
        self.algo_select.setItemText(3, QCoreApplication.translate("network_ui", u"LoHa", None))
        self.algo_select.setItemText(4, QCoreApplication.translate("network_ui", u"IA3", None))
        self.algo_select.setItemText(5, QCoreApplication.translate("network_ui", u"Lokr", None))
        self.algo_select.setItemText(6, QCoreApplication.translate("network_ui", u"DyLoRA", None))

#if QT_CONFIG(tooltip)
        self.algo_select.setToolTip(QCoreApplication.translate("network_ui", u"<html><head/><body><p>The algorithm that is used for training, LoRA is the only one that doesn't train on all layers. LoCon is just LoRA that train on all layers LoHa has a ton of compression, and that is basically true for ia3 and Lokr as well. DyLora is a type of LoRA (or LoCon) that basically allows you to train multiple dim sized models in one, it does take a lot longer to train.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.network_dim_label.setText(QCoreApplication.translate("network_ui", u"Network Dimension", None))
#if QT_CONFIG(tooltip)
        self.network_dim_input.setToolTip(QCoreApplication.translate("network_ui", u"<html><head/><body><p>The dimension of the model, the higher the dim the larger the file size. Keep in mind that larger does not mean better. I suggest you keep the dim low.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.network_alpha_label.setText(QCoreApplication.translate("network_ui", u"Network Alpha", None))
#if QT_CONFIG(tooltip)
        self.network_alpha_input.setToolTip(QCoreApplication.translate("network_ui", u"<html><head/><body><p>The scalar of the dim. Basically, if you have an alpha of 16 and a dim of 32, then the scalar is 0.5 which is a multiplier on the weights. I suggest you use half dim for alpha, in any case other than less than dim 9, in which I suggest you use alpha 1.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.conv_dim_label.setText(QCoreApplication.translate("network_ui", u"Conv Dimension", None))
#if QT_CONFIG(tooltip)
        self.conv_dim_input.setToolTip(QCoreApplication.translate("network_ui", u"<html><head/><body><p>The dimension size for the conv layers. These layers carry more style with them, so be careful about setting them too high. I personally suggest you never go higher than 32 with them.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.conv_alpha_label.setText(QCoreApplication.translate("network_ui", u"Conv Alpha", None))
#if QT_CONFIG(tooltip)
        self.conv_alpha_input.setToolTip(QCoreApplication.translate("network_ui", u"<html><head/><body><p>The scalar of the conv dims. Much like the normal dim, I suggest you use half conv dim, or 1 if the dim size is 8 or lower.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dylora_unit_label.setText(QCoreApplication.translate("network_ui", u"DyLoRA Unit", None))
#if QT_CONFIG(tooltip)
        self.dylora_unit_input.setToolTip(QCoreApplication.translate("network_ui", u"<html><head/><body><p>The unit is the unit for dividing rank. so if you have dim 16, unit 4, then it can learn 4 lora models of dims 4, 8, 12, and 16.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lyco_dropout_enable.setText(QCoreApplication.translate("network_ui", u"Lyco Dropout", None))
#if QT_CONFIG(tooltip)
        self.lyco_dropout_input.setToolTip(QCoreApplication.translate("network_ui", u"<html><head/><body><p>Dropout from LyCORIS. Not clearly explained in the readme, not entirely sure what it does.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cp_enable.setToolTip(QCoreApplication.translate("network_ui", u"<html><head/><body><p>Enables Conv CP, which is some form of compression algorithm that further reduces file size, I personally suggest you don't use it</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cp_enable.setText(QCoreApplication.translate("network_ui", u"Enable Conv CP", None))
        self.unet_te_both_label.setText(QCoreApplication.translate("network_ui", u"Train on", None))
        self.unet_te_both_select.setItemText(0, QCoreApplication.translate("network_ui", u"Both", None))
        self.unet_te_both_select.setItemText(1, QCoreApplication.translate("network_ui", u"Unet Only", None))
        self.unet_te_both_select.setItemText(2, QCoreApplication.translate("network_ui", u"TE Only", None))

#if QT_CONFIG(tooltip)
        self.unet_te_both_select.setToolTip(QCoreApplication.translate("network_ui", u"<html><head/><body><p>You can train on both the text encoder and unet or only one or the other, most of the time you want to train on both.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.network_dropout_enable.setText(QCoreApplication.translate("network_ui", u"Network Dropout", None))
#if QT_CONFIG(tooltip)
        self.network_dropout_input.setToolTip(QCoreApplication.translate("network_ui", u"<html><head/><body><p>Is a random chance that on any given step a neuron will be dropped out, encourages the model to diversify it's training </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rank_dropout_enable.setText(QCoreApplication.translate("network_ui", u"Rank Dropout", None))
#if QT_CONFIG(tooltip)
        self.rank_dropout_input.setToolTip(QCoreApplication.translate("network_ui", u"<html><head/><body><p>Dropouts each dim of a lora at the rate specified, This is unproven, use at your own risk.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.module_dropout_enable.setText(QCoreApplication.translate("network_ui", u"Module Dropout", None))
#if QT_CONFIG(tooltip)
        self.module_dropout_input.setToolTip(QCoreApplication.translate("network_ui", u"<html><head/><body><p>Drops out each module at the specified probability. Module dropout has not be verified, use at your own risk.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), QCoreApplication.translate("network_ui", u"Main Args", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.block_weight_tab), QCoreApplication.translate("network_ui", u"Block Weights", None))
    # retranslateUi

