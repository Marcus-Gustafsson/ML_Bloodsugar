# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'User_input_static.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDialog, QDialogButtonBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_static_dialog(object):
    def setupUi(self, static_dialog):
        if not static_dialog.objectName():
            static_dialog.setObjectName(u"static_dialog")
        static_dialog.resize(616, 286)
        static_dialog.setStyleSheet(u"QWidget {\n"
"    background-color: #2D2D30;\n"
"    color: #CCCCCC;\n"
"}\n"
"\n"
"QLabel, QCheckBox {\n"
"    color: #D0D0D0;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #0078D7; /* Adjust the color code to match the blue you desire */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    padding: 5px;\n"
"    margin: 2px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #005FA3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003A70;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #004C99;\n"
"    color: #7F7F7F;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #2D2D30;\n"
"    border: 1px solid #555;\n"
"    border-radius: 2px;\n"
"    color: #D0D0D0;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 1px solid #555;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 7px;\n"
"    background-color: #2D2D30;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked "
                        "{\n"
"    background-color: #3A3A3C;\n"
"    border: 1px solid #3A3A3C;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #444;\n"
"    height: 8px;\n"
"    background: #2D2D30;\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #3A3A3C;\n"
"    border: 1px solid #5C5C5C;\n"
"    width: 18px;\n"
"    margin: -2px 0;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #555;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #3A3A3C;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(static_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(static_dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_user_name = QGroupBox(self.groupBox)
        self.groupBox_user_name.setObjectName(u"groupBox_user_name")
        self.groupBox_user_name.setAlignment(Qt.AlignCenter)
        self.gridLayout_3 = QGridLayout(self.groupBox_user_name)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_user_name = QLineEdit(self.groupBox_user_name)
        self.lineEdit_user_name.setObjectName(u"lineEdit_user_name")

        self.gridLayout_3.addWidget(self.lineEdit_user_name, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_user_name)

        self.groupBox_date_of_birth = QGroupBox(self.groupBox)
        self.groupBox_date_of_birth.setObjectName(u"groupBox_date_of_birth")
        self.groupBox_date_of_birth.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox_date_of_birth)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dateEdit_date_of_birth = QDateEdit(self.groupBox_date_of_birth)
        self.dateEdit_date_of_birth.setObjectName(u"dateEdit_date_of_birth")

        self.gridLayout.addWidget(self.dateEdit_date_of_birth, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_date_of_birth)

        self.groupBox_weight = QGroupBox(self.groupBox)
        self.groupBox_weight.setObjectName(u"groupBox_weight")
        self.groupBox_weight.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox_weight)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_weight = QLineEdit(self.groupBox_weight)
        self.lineEdit_weight.setObjectName(u"lineEdit_weight")

        self.gridLayout_2.addWidget(self.lineEdit_weight, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_weight)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(static_dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.groupBox_insulin_type = QGroupBox(self.groupBox_2)
        self.groupBox_insulin_type.setObjectName(u"groupBox_insulin_type")
        self.groupBox_insulin_type.setAlignment(Qt.AlignCenter)
        self.gridLayout_4 = QGridLayout(self.groupBox_insulin_type)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.comboBox_insulin_type = QComboBox(self.groupBox_insulin_type)
        self.comboBox_insulin_type.addItem("")
        self.comboBox_insulin_type.addItem("")
        self.comboBox_insulin_type.setObjectName(u"comboBox_insulin_type")

        self.gridLayout_4.addWidget(self.comboBox_insulin_type, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_insulin_type)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.groupBox_insulin_to_carb_ratio = QGroupBox(self.groupBox_2)
        self.groupBox_insulin_to_carb_ratio.setObjectName(u"groupBox_insulin_to_carb_ratio")
        self.groupBox_insulin_to_carb_ratio.setAlignment(Qt.AlignCenter)
        self.gridLayout_5 = QGridLayout(self.groupBox_insulin_to_carb_ratio)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit_insulin_to_carb_ratio = QLineEdit(self.groupBox_insulin_to_carb_ratio)
        self.lineEdit_insulin_to_carb_ratio.setObjectName(u"lineEdit_insulin_to_carb_ratio")

        self.gridLayout_5.addWidget(self.lineEdit_insulin_to_carb_ratio, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_insulin_to_carb_ratio)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.groupBox_blood_sugar_unit = QGroupBox(self.groupBox_2)
        self.groupBox_blood_sugar_unit.setObjectName(u"groupBox_blood_sugar_unit")
        self.groupBox_blood_sugar_unit.setAlignment(Qt.AlignCenter)
        self.gridLayout_6 = QGridLayout(self.groupBox_blood_sugar_unit)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.checkBox_mmol_unit = QCheckBox(self.groupBox_blood_sugar_unit)
        self.checkBox_mmol_unit.setObjectName(u"checkBox_mmol_unit")

        self.gridLayout_6.addWidget(self.checkBox_mmol_unit, 0, 0, 1, 1)

        self.checkBox_mg_dl_unit = QCheckBox(self.groupBox_blood_sugar_unit)
        self.checkBox_mg_dl_unit.setObjectName(u"checkBox_mg_dl_unit")

        self.gridLayout_6.addWidget(self.checkBox_mg_dl_unit, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_blood_sugar_unit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.buttonBox_ok_cancel = QDialogButtonBox(static_dialog)
        self.buttonBox_ok_cancel.setObjectName(u"buttonBox_ok_cancel")
        self.buttonBox_ok_cancel.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox_ok_cancel.setOrientation(Qt.Horizontal)
        self.buttonBox_ok_cancel.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox_ok_cancel.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox_ok_cancel)


        self.retranslateUi(static_dialog)
        self.buttonBox_ok_cancel.accepted.connect(static_dialog.accept)
        self.buttonBox_ok_cancel.rejected.connect(static_dialog.reject)

        QMetaObject.connectSlotsByName(static_dialog)
    # setupUi

    def retranslateUi(self, static_dialog):
        static_dialog.setWindowTitle(QCoreApplication.translate("static_dialog", u"Dialog", None))
        self.groupBox.setTitle("")
        self.groupBox_user_name.setTitle(QCoreApplication.translate("static_dialog", u"First name", None))
        self.groupBox_date_of_birth.setTitle(QCoreApplication.translate("static_dialog", u"Date of birth", None))
        self.groupBox_weight.setTitle(QCoreApplication.translate("static_dialog", u"Weight (kg)", None))
        self.groupBox_2.setTitle("")
        self.groupBox_insulin_type.setTitle(QCoreApplication.translate("static_dialog", u"Insulin type", None))
        self.comboBox_insulin_type.setItemText(0, QCoreApplication.translate("static_dialog", u"Fiasp", None))
        self.comboBox_insulin_type.setItemText(1, QCoreApplication.translate("static_dialog", u"Novorapid", None))

        self.groupBox_insulin_to_carb_ratio.setTitle(QCoreApplication.translate("static_dialog", u"Insulin-to-carb ratio (grams)", None))
        self.groupBox_blood_sugar_unit.setTitle(QCoreApplication.translate("static_dialog", u"Blood sugar unit", None))
        self.checkBox_mmol_unit.setText(QCoreApplication.translate("static_dialog", u"mmol/L", None))
        self.checkBox_mg_dl_unit.setText(QCoreApplication.translate("static_dialog", u"mg/dL", None))
    # retranslateUi

