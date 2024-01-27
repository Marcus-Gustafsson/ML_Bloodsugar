# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QGroupBox,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(704, 614)
        MainWindow.setStyleSheet(u"QWidget {\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.GB_mainwindow = QGroupBox(self.centralwidget)
        self.GB_mainwindow.setObjectName(u"GB_mainwindow")
        self.verticalLayout = QVBoxLayout(self.GB_mainwindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_app_title = QLineEdit(self.GB_mainwindow)
        self.lineEdit_app_title.setObjectName(u"lineEdit_app_title")

        self.verticalLayout.addWidget(self.lineEdit_app_title)

        self.gb_graph_and_user = QGroupBox(self.GB_mainwindow)
        self.gb_graph_and_user.setObjectName(u"gb_graph_and_user")
        self.verticalLayout_2 = QVBoxLayout(self.gb_graph_and_user)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_current_user = QLineEdit(self.gb_graph_and_user)
        self.lineEdit_current_user.setObjectName(u"lineEdit_current_user")

        self.verticalLayout_2.addWidget(self.lineEdit_current_user)

        self.GB_user = QGroupBox(self.gb_graph_and_user)
        self.GB_user.setObjectName(u"GB_user")
        self.gridLayout_2 = QGridLayout(self.GB_user)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb_new_user = QPushButton(self.GB_user)
        self.pb_new_user.setObjectName(u"pb_new_user")

        self.gridLayout_2.addWidget(self.pb_new_user, 0, 0, 1, 1)

        self.pb_daily_values = QPushButton(self.GB_user)
        self.pb_daily_values.setObjectName(u"pb_daily_values")

        self.gridLayout_2.addWidget(self.pb_daily_values, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.GB_user)


        self.verticalLayout.addWidget(self.gb_graph_and_user)

        self.GB_graphviewer = QGroupBox(self.GB_mainwindow)
        self.GB_graphviewer.setObjectName(u"GB_graphviewer")
        self.gridLayout_3 = QGridLayout(self.GB_graphviewer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.graphicsView_blood_insulin_graph = QGraphicsView(self.GB_graphviewer)
        self.graphicsView_blood_insulin_graph.setObjectName(u"graphicsView_blood_insulin_graph")

        self.gridLayout_3.addWidget(self.graphicsView_blood_insulin_graph, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.GB_graphviewer)


        self.gridLayout.addWidget(self.GB_mainwindow, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 704, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.GB_mainwindow.setTitle("")
        self.lineEdit_app_title.setText(QCoreApplication.translate("MainWindow", u"Blood sugar prediction", None))
        self.gb_graph_and_user.setTitle("")
        self.lineEdit_current_user.setText(QCoreApplication.translate("MainWindow", u"Current user", None))
        self.GB_user.setTitle(QCoreApplication.translate("MainWindow", u"User", None))
        self.pb_new_user.setText(QCoreApplication.translate("MainWindow", u"New User", None))
        self.pb_daily_values.setText(QCoreApplication.translate("MainWindow", u"Input Daily Values", None))
        self.GB_graphviewer.setTitle(QCoreApplication.translate("MainWindow", u"Graphviewer", None))
    # retranslateUi

