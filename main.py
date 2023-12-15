import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap, QBrush


class Git(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        uic.loadUi('UI.ui', self)
        self.setFixedSize(800, 570)
        self.drawCircleButton.clicked.connect(self.drawCircle)
        canvas = QPixmap(800, 570)
        self.label.setPixmap(canvas)

    def drawCircle(self):
        x, y = [randint(10, 500) for x in range(2)]
        w = randint(10, 100)
        h = w
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(Qt.yellow)
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))

        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Git()
    ex.show()
    sys.exit(app.exec_())
