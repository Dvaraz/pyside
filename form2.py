# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 673)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setIconSize(QSize(16, 16))
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout.addWidget(self.pushButton_6)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")

        self.horizontalLayout_3.addWidget(self.dial)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout_2.addWidget(self.lcdNumber)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.horizontalSlider)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_4.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1020, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton_5.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0432\u043e/\u041d\u0438\u0437", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043e/\u043d\u0438\u0437", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e\u043a\u043d\u0430", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"HEX", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"DEC", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"BIT", None))

    # retranslateUi
    #
    # def event(self, event: QEvent) -> bool:
    #
    #     if event.type() ==


class MainTestWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.app_width = QWidget.width(self)
        self.app_height = QWidget.height(self)
        self.screen_width = QApplication.primaryScreen().size().width()
        self.screen_height = QApplication.primaryScreen().size().height()

        self.ui.pushButton.clicked.connect(self.left_top)
        self.ui.pushButton_2.clicked.connect(self.right_top)
        self.ui.pushButton_3.clicked.connect(self.center)
        self.ui.pushButton_4.clicked.connect(self.left_bot)
        self.ui.pushButton_5.clicked.connect(self.right_bot)

        self.ui.pushButton_6.clicked.connect(self.get_information)


    def dial(self):
        print("dial")


    def left_top(self):
        self.move(0, 0)

    def right_top(self):
        self.move(self.screen_width - self.app_width, 0)

    def center(self):
        self.move((self.screen_width/2) - (self.app_width/2), (self.screen_height/2) - (self.app_height/2))

    def left_bot(self):
        self.move(0, self.screen_height - self.app_height)

    def right_bot(self):
        self.move(self.screen_width - self.app_width, self.screen_height - self.app_height)

    def get_information(self):
        screens_count = QApplication.screens()

        log = self.ui.textEdit.append

        log(str(time.ctime()))

        log(f"Number of displays {len(screens_count)}")

        for screen in screens_count:
            log(f"{screen.name()}")
            log(f"Size of the display width : {screen.size().width()} height: {screen.size().height()}")




if __name__ == '__main__':
    app = QApplication()

    window = MainTestWindow()
    window.show()

    app.exec_()