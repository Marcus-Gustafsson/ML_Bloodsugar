# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'User_input_daily.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_daily_dialog(object):
    def setupUi(self, daily_dialog):
        if not daily_dialog.objectName():
            daily_dialog.setObjectName(u"daily_dialog")
        daily_dialog.resize(658, 517)
        daily_dialog.setLayoutDirection(Qt.LeftToRight)
        daily_dialog.setStyleSheet(u"QWidget {\n"
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
        self.verticalLayout = QVBoxLayout(daily_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(daily_dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_carb_low = QPushButton(self.groupBox)
        self.pb_carb_low.setObjectName(u"pb_carb_low")

        self.horizontalLayout.addWidget(self.pb_carb_low)

        self.pb_carb_medium = QPushButton(self.groupBox)
        self.pb_carb_medium.setObjectName(u"pb_carb_medium")

        self.horizontalLayout.addWidget(self.pb_carb_medium)

        self.pb_carb_high = QPushButton(self.groupBox)
        self.pb_carb_high.setObjectName(u"pb_carb_high")

        self.horizontalLayout.addWidget(self.pb_carb_high)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(daily_dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_fat_low = QPushButton(self.groupBox_2)
        self.pb_fat_low.setObjectName(u"pb_fat_low")

        self.horizontalLayout_2.addWidget(self.pb_fat_low)

        self.pb_fat_medium = QPushButton(self.groupBox_2)
        self.pb_fat_medium.setObjectName(u"pb_fat_medium")

        self.horizontalLayout_2.addWidget(self.pb_fat_medium)

        self.pb_fat_high = QPushButton(self.groupBox_2)
        self.pb_fat_high.setObjectName(u"pb_fat_high")

        self.horizontalLayout_2.addWidget(self.pb_fat_high)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(daily_dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pb_protein_low = QPushButton(self.groupBox_3)
        self.pb_protein_low.setObjectName(u"pb_protein_low")

        self.horizontalLayout_3.addWidget(self.pb_protein_low)

        self.pb_protein_medium = QPushButton(self.groupBox_3)
        self.pb_protein_medium.setObjectName(u"pb_protein_medium")

        self.horizontalLayout_3.addWidget(self.pb_protein_medium)

        self.pb_protein_high = QPushButton(self.groupBox_3)
        self.pb_protein_high.setObjectName(u"pb_protein_high")

        self.horizontalLayout_3.addWidget(self.pb_protein_high)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(daily_dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pb_exercise_no = QPushButton(self.groupBox_4)
        self.pb_exercise_no.setObjectName(u"pb_exercise_no")

        self.horizontalLayout_4.addWidget(self.pb_exercise_no)

        self.pb_exercise_light = QPushButton(self.groupBox_4)
        self.pb_exercise_light.setObjectName(u"pb_exercise_light")

        self.horizontalLayout_4.addWidget(self.pb_exercise_light)

        self.pb_exercise_medium = QPushButton(self.groupBox_4)
        self.pb_exercise_medium.setObjectName(u"pb_exercise_medium")

        self.horizontalLayout_4.addWidget(self.pb_exercise_medium)

        self.pb_exercise_high = QPushButton(self.groupBox_4)
        self.pb_exercise_high.setObjectName(u"pb_exercise_high")

        self.horizontalLayout_4.addWidget(self.pb_exercise_high)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(daily_dialog)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineedit_insulin_dose = QLineEdit(self.groupBox_6)
        self.lineedit_insulin_dose.setObjectName(u"lineedit_insulin_dose")

        self.gridLayout.addWidget(self.lineedit_insulin_dose, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.timeEdit_time_of_insulin = QTimeEdit(self.groupBox_7)
        self.timeEdit_time_of_insulin.setObjectName(u"timeEdit_time_of_insulin")

        self.gridLayout_2.addWidget(self.timeEdit_time_of_insulin, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.groupBox_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setAlignment(Qt.AlignCenter)
        self.gridLayout_3 = QGridLayout(self.groupBox_8)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_blood_sugar = QLineEdit(self.groupBox_8)
        self.lineEdit_blood_sugar.setObjectName(u"lineEdit_blood_sugar")

        self.gridLayout_3.addWidget(self.lineEdit_blood_sugar, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.groupBox_5)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setAlignment(Qt.AlignCenter)
        self.gridLayout_4 = QGridLayout(self.groupBox_9)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.timeEdit_blood_sugar = QTimeEdit(self.groupBox_9)
        self.timeEdit_blood_sugar.setObjectName(u"timeEdit_blood_sugar")

        self.gridLayout_4.addWidget(self.timeEdit_blood_sugar, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.groupBox_9)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.ok_cancel_button_box = QDialogButtonBox(daily_dialog)
        self.ok_cancel_button_box.setObjectName(u"ok_cancel_button_box")
        self.ok_cancel_button_box.setLayoutDirection(Qt.LeftToRight)
        self.ok_cancel_button_box.setOrientation(Qt.Horizontal)
        self.ok_cancel_button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.ok_cancel_button_box, 0, Qt.AlignHCenter)


        self.retranslateUi(daily_dialog)
        self.ok_cancel_button_box.accepted.connect(daily_dialog.accept)
        self.ok_cancel_button_box.rejected.connect(daily_dialog.reject)

        QMetaObject.connectSlotsByName(daily_dialog)
    # setupUi

    def retranslateUi(self, daily_dialog):
        daily_dialog.setWindowTitle(QCoreApplication.translate("daily_dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("daily_dialog", u"Carb content", None))
        self.pb_carb_low.setText(QCoreApplication.translate("daily_dialog", u"Low", None))
        self.pb_carb_medium.setText(QCoreApplication.translate("daily_dialog", u"Medium", None))
        self.pb_carb_high.setText(QCoreApplication.translate("daily_dialog", u"High", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("daily_dialog", u"Fat content", None))
        self.pb_fat_low.setText(QCoreApplication.translate("daily_dialog", u"Low", None))
        self.pb_fat_medium.setText(QCoreApplication.translate("daily_dialog", u"Medium", None))
        self.pb_fat_high.setText(QCoreApplication.translate("daily_dialog", u"High", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("daily_dialog", u"Protein content", None))
        self.pb_protein_low.setText(QCoreApplication.translate("daily_dialog", u"Low", None))
        self.pb_protein_medium.setText(QCoreApplication.translate("daily_dialog", u"Medium", None))
        self.pb_protein_high.setText(QCoreApplication.translate("daily_dialog", u"High", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("daily_dialog", u"Exercise intensity next 90 minutes", None))
        self.pb_exercise_no.setText(QCoreApplication.translate("daily_dialog", u"No", None))
        self.pb_exercise_light.setText(QCoreApplication.translate("daily_dialog", u"Light", None))
        self.pb_exercise_medium.setText(QCoreApplication.translate("daily_dialog", u"Medium", None))
        self.pb_exercise_high.setText(QCoreApplication.translate("daily_dialog", u"High", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("daily_dialog", u"Insulin and blood sugar", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("daily_dialog", u"Insulin dose (units)", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("daily_dialog", u"Time of dose", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("daily_dialog", u"Blood sugar reading", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("daily_dialog", u"Time of reading", None))
    # retranslateUi

