# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'threads.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1099, 756)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.timer = QLabel(self.frame)
        self.timer.setObjectName(u"timer")
        sizePolicy.setHeightForWidth(self.timer.sizePolicy().hasHeightForWidth())
        self.timer.setSizePolicy(sizePolicy)
        self.timer.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.timer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.set_time = QLabel(self.frame)
        self.set_time.setObjectName(u"set_time")
        sizePolicy.setHeightForWidth(self.set_time.sizePolicy().hasHeightForWidth())
        self.set_time.setSizePolicy(sizePolicy)
        self.set_time.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.set_time)

        self.set_time_spinBox = QSpinBox(self.frame)
        self.set_time_spinBox.setObjectName(u"set_time_spinBox")
        sizePolicy.setHeightForWidth(self.set_time_spinBox.sizePolicy().hasHeightForWidth())
        self.set_time_spinBox.setSizePolicy(sizePolicy)
        self.set_time_spinBox.setMaximumSize(QSize(50, 30))
        self.set_time_spinBox.setMinimum(5)

        self.horizontalLayout_3.addWidget(self.set_time_spinBox)

        self.sec_1 = QLabel(self.frame)
        self.sec_1.setObjectName(u"sec_1")
        sizePolicy.setHeightForWidth(self.sec_1.sizePolicy().hasHeightForWidth())
        self.sec_1.setSizePolicy(sizePolicy)
        self.sec_1.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.sec_1)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.start_pushButton = QPushButton(self.frame)
        self.start_pushButton.setObjectName(u"start_pushButton")
        sizePolicy.setHeightForWidth(self.start_pushButton.sizePolicy().hasHeightForWidth())
        self.start_pushButton.setSizePolicy(sizePolicy)
        self.start_pushButton.setMaximumSize(QSize(4000, 30))

        self.verticalLayout.addWidget(self.start_pushButton)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.time_left = QLabel(self.frame)
        self.time_left.setObjectName(u"time_left")
        sizePolicy.setHeightForWidth(self.time_left.sizePolicy().hasHeightForWidth())
        self.time_left.setSizePolicy(sizePolicy)
        self.time_left.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.time_left)

        self.time_left_lineEdit = QLineEdit(self.frame)
        self.time_left_lineEdit.setObjectName(u"time_left_lineEdit")
        sizePolicy.setHeightForWidth(self.time_left_lineEdit.sizePolicy().hasHeightForWidth())
        self.time_left_lineEdit.setSizePolicy(sizePolicy)
        self.time_left_lineEdit.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_4.addWidget(self.time_left_lineEdit)

        self.sec_2 = QLabel(self.frame)
        self.sec_2.setObjectName(u"sec_2")
        sizePolicy.setHeightForWidth(self.sec_2.sizePolicy().hasHeightForWidth())
        self.sec_2.setSizePolicy(sizePolicy)
        self.sec_2.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.sec_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 428, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.availability = QLabel(self.frame_2)
        self.availability.setObjectName(u"availability")
        sizePolicy.setHeightForWidth(self.availability.sizePolicy().hasHeightForWidth())
        self.availability.setSizePolicy(sizePolicy)
        self.availability.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.availability)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.URL = QLabel(self.frame_2)
        self.URL.setObjectName(u"URL")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.URL.sizePolicy().hasHeightForWidth())
        self.URL.setSizePolicy(sizePolicy1)
        self.URL.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_5.addWidget(self.URL)

        self.url_lineEdit = QLineEdit(self.frame_2)
        self.url_lineEdit.setObjectName(u"url_lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.url_lineEdit.sizePolicy().hasHeightForWidth())
        self.url_lineEdit.setSizePolicy(sizePolicy2)
        self.url_lineEdit.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_5.addWidget(self.url_lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_6.addWidget(self.label_9)

        self.check_spinBox_2 = QSpinBox(self.frame_2)
        self.check_spinBox_2.setObjectName(u"check_spinBox_2")
        sizePolicy.setHeightForWidth(self.check_spinBox_2.sizePolicy().hasHeightForWidth())
        self.check_spinBox_2.setSizePolicy(sizePolicy)
        self.check_spinBox_2.setMaximumSize(QSize(16777215, 30))
        self.check_spinBox_2.setMinimum(5)

        self.horizontalLayout_6.addWidget(self.check_spinBox_2)

        self.sec_3 = QLabel(self.frame_2)
        self.sec_3.setObjectName(u"sec_3")
        sizePolicy.setHeightForWidth(self.sec_3.sizePolicy().hasHeightForWidth())
        self.sec_3.setSizePolicy(sizePolicy)
        self.sec_3.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_6.addWidget(self.sec_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.url_start_button = QPushButton(self.frame_2)
        self.url_start_button.setObjectName(u"url_start_button")

        self.verticalLayout_2.addWidget(self.url_start_button)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)

        self.log_plainTextEdit = QPlainTextEdit(self.frame_2)
        self.log_plainTextEdit.setObjectName(u"log_plainTextEdit")

        self.verticalLayout_2.addWidget(self.log_plainTextEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.system_label = QLabel(self.frame_3)
        self.system_label.setObjectName(u"system_label")
        sizePolicy.setHeightForWidth(self.system_label.sizePolicy().hasHeightForWidth())
        self.system_label.setSizePolicy(sizePolicy)
        self.system_label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.system_label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_7.addWidget(self.label_12)

        self.refresh_spinBox = QSpinBox(self.frame_3)
        self.refresh_spinBox.setObjectName(u"refresh_spinBox")
        self.refresh_spinBox.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_7.addWidget(self.refresh_spinBox)

        self.sec_4 = QLabel(self.frame_3)
        self.sec_4.setObjectName(u"sec_4")
        sizePolicy.setHeightForWidth(self.sec_4.sizePolicy().hasHeightForWidth())
        self.sec_4.setSizePolicy(sizePolicy)
        self.sec_4.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_7.addWidget(self.sec_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cpu_label = QLabel(self.frame_3)
        self.cpu_label.setObjectName(u"cpu_label")
        sizePolicy.setHeightForWidth(self.cpu_label.sizePolicy().hasHeightForWidth())
        self.cpu_label.setSizePolicy(sizePolicy)
        self.cpu_label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_4.addWidget(self.cpu_label)

        self.cpu_progressBar = QProgressBar(self.frame_3)
        self.cpu_progressBar.setObjectName(u"cpu_progressBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cpu_progressBar.sizePolicy().hasHeightForWidth())
        self.cpu_progressBar.setSizePolicy(sizePolicy3)
        self.cpu_progressBar.setLayoutDirection(Qt.LeftToRight)
        self.cpu_progressBar.setValue(12)
        self.cpu_progressBar.setTextVisible(True)
        self.cpu_progressBar.setOrientation(Qt.Vertical)

        self.verticalLayout_4.addWidget(self.cpu_progressBar)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ram_label = QLabel(self.frame_3)
        self.ram_label.setObjectName(u"ram_label")
        sizePolicy.setHeightForWidth(self.ram_label.sizePolicy().hasHeightForWidth())
        self.ram_label.setSizePolicy(sizePolicy)
        self.ram_label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_5.addWidget(self.ram_label)

        self.ram_progressBar = QProgressBar(self.frame_3)
        self.ram_progressBar.setObjectName(u"ram_progressBar")
        sizePolicy3.setHeightForWidth(self.ram_progressBar.sizePolicy().hasHeightForWidth())
        self.ram_progressBar.setSizePolicy(sizePolicy3)
        self.ram_progressBar.setValue(24)
        self.ram_progressBar.setTextVisible(True)
        self.ram_progressBar.setOrientation(Qt.Vertical)
        self.ram_progressBar.setInvertedAppearance(False)
        self.ram_progressBar.setTextDirection(QProgressBar.BottomToTop)

        self.verticalLayout_5.addWidget(self.ram_progressBar)


        self.horizontalLayout_8.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.horizontalLayout.addWidget(self.frame_3)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1099, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.timer.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.set_time.setText(QCoreApplication.translate("MainWindow", u"Set time", None))
        self.sec_1.setText(QCoreApplication.translate("MainWindow", u"sec.", None))
        self.start_pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.time_left.setText(QCoreApplication.translate("MainWindow", u"Time left", None))
        self.sec_2.setText(QCoreApplication.translate("MainWindow", u"sec.", None))
        self.availability.setText(QCoreApplication.translate("MainWindow", u"URL availability", None))
        self.URL.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"check every", None))
        self.sec_3.setText(QCoreApplication.translate("MainWindow", u"sec", None))
        self.url_start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Log:", None))
        self.system_label.setText(QCoreApplication.translate("MainWindow", u"System status", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"refresh every", None))
        self.sec_4.setText(QCoreApplication.translate("MainWindow", u"sec.", None))
        self.cpu_label.setText(QCoreApplication.translate("MainWindow", u"CPU:", None))
        self.ram_label.setText(QCoreApplication.translate("MainWindow", u"RAM:", None))
    # retranslateUi

