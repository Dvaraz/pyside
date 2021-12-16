from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtNetwork import *
import requests
import time

from threads_p_3 import Ui_MainWindow


class MainTestWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.thread_1 = ThreadP()
        self.thread_status = Thread_Status()

        self.ui.start_pushButton.clicked.connect(self.start_timer)

        self.ui.start_pushButton.clicked.connect(self.stopThread)

        self.thread_1.mysignal.connect(self.time_left_line_edit, Qt.AutoConnection)

        self.ui.url_lineEdit.setText("https://www.google.ru/")
        self.ui.url_start_button.clicked.connect(self.start_status)
        self.ui.url_start_button.clicked.connect(self.stopThread)
        self.thread_status.mysignal.connect(self.check_status, Qt.AutoConnection)

    def check_status(self, text):
        self.ui.log_plainTextEdit.appendPlainText(f"{time.ctime()} status - {text}")

    def start_status(self):
        self.thread_status.started.connect(lambda: self.ui.url_start_button.setText("stop"))
        self.thread_status.finished.connect(lambda: self.ui.url_start_button.setText("start"))
        self.thread_status.set_url(self.ui.url_lineEdit.text())
        self.thread_status.set_timer(self.ui.check_spinBox_2.value())
        self.thread_status.start()

    def start_timer(self):
        self.thread_1.started.connect(lambda: self.ui.start_pushButton.setText("stop"))
        self.thread_1.finished.connect(lambda: self.ui.start_pushButton.setText("start"))
        self.thread_1.set_param(self.ui.set_time_spinBox.value())
        self.thread_1.start()

    def time_left_line_edit(self, text):
        self.ui.time_left_lineEdit.setText(text)

    def stopThread(self):
        self.thread_1.status = False


class ThreadP(QThread):
    mysignal = Signal(str)

    def set_param(self, count):
        self.count = count

    def run(self) -> None:
        self.status = True
        while self.status:
            time.sleep(1)
            self.mysignal.emit(str(self.count))
            self.count -= 1
            if self.count == 0:
                break


class Thread_Status(QThread):
    mysignal = Signal(str)

    def set_url(self, url):
        self.url = url

    def set_timer(self, sec):
        self.sec = int(sec)

    def run(self) -> None:
        self.status = True
        while self.status:
            self.mysignal.emit(str(requests.get(self.url).status_code))
            time.sleep(self.sec)


if __name__ == '__main__':
    app = QApplication()

    window = MainTestWindow()
    window.show()

    app.exec_()