from PySide2 import QtWidgets, QtCore


class MainTestWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lineEditSurname = QtWidgets.QLineEdit()
        self.lineEditSurname.setPlaceholderText("Фамилия")
        self.lineEditFirstName = QtWidgets.QLineEdit()
        self.lineEditFirstName.setPlaceholderText("Имя")
        self.lineEditTel = QtWidgets.QLineEdit()
        self.lineEditTel.setPlaceholderText("Телефон")

        self.pushButtonOk = QtWidgets.QPushButton("Ok")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEditFirstName)
        layout.addWidget(self.lineEditSurname)
        layout.addWidget(self.lineEditTel)
        layout.addWidget(self.pushButtonOk)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()

    app.exec_()