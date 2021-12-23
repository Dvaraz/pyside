import sys
from PySide2 import QtGui, QtCore, QtWidgets
import random
from math import cos


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test")
        self.setGeometry(300, 200, 640, 520)
        # self.setFixedSize(640, 520)
        self.create_ui()

        self.show()


    def resizeEvent(self, event:QtGui.QResizeEvent) -> None:
        self.view.scene().setSceneRect(0, 0, self.size().width() - 10, self.size().height() - 10)
        a = self.view.scene().items()[0]
        a.setRect(100, 30, 300, 300, )


    def create_ui(self):
        scene = QtWidgets.QGraphicsScene(self)
        scene.setSceneRect(0, 0, self.size().width() - 10, self.size().height() - 10)
        brush = QtGui.QBrush(QtCore.Qt.blue)
        brush2 = QtGui.QBrush(QtCore.Qt.gray)
        brush3 = QtGui.QBrush(QtCore.Qt.green)
        pen = QtGui.QPen(QtCore.Qt.black)
        pen.setWidth(2)

        rect1 = scene.addRect(0, 0, 30, 30, pen, brush)
        rect2 = scene.addRect(50, 30, 30, 30, pen, brush2)
        rect3 = scene.addRect(100, 30, 30, 30, pen, brush3)
        rect1.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        rect2.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        rect3.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)


        self.view = QtWidgets.QGraphicsView(scene, self)
        self.setCentralWidget(self.view)

    def keyPressEvent(self, event:QtGui.QKeyEvent) -> None:
        event.key()
        if event.key() == QtCore.Qt.Key_W:
            a = self.view.scene().items()[0]
            a.moveBy(10, 10)
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())