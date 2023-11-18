import random
import sys
from math import cos, sin, pi

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('РЕЗНЯЯЯ')
        self.setMouseTracking(True)
        self.qp = QPainter()
        self.status = None
        self.coords = None

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw()
        self.qp.end()

    def draw(self):
        if self.status == 1:
            r = random.randint(20, 100)
            self.qp.setBrush(QColor(*[random.randint(0, 255) for _ in range(3)]))
            self.qp.drawEllipse(int(self.coords[0] - r / 2), int(self.coords[1] - r / 2), r, r)

        elif self.status == 2:
            s = random.randint(20, 100)
            self.qp.setBrush(QColor(*[random.randint(0, 255) for _ in range(3)]))
            self.qp.drawRect(int(self.coords[0] - s / 2), int(self.coords[1] - s / 2), s, s)

        elif self.status == 3:
            x, y = self.coords
            A = random.randint(20, 100)

            coords = [QPoint(x, y - A),
                      QPoint(int(x + cos(7 * pi / 6) * A),
                             int(y - sin(7 * pi / 6) * A)),
                      QPoint(int(x + cos(11 * pi / 6) * A),
                             int(y - sin(11 * pi / 6) * A))]
            self.qp.setBrush(QColor(*[random.randint(0, 255) for _ in range(3)]))
            self.qp.drawPolygon(coords)

    def mouseMoveEvent(self, event):
        self.coords = (event.x(), event.y())

    def mousePressEvent(self, event):
        self.coords = (event.x(), event.y())
        if event.button() == Qt.LeftButton:
            self.status = 1
        if event.button() == Qt.RightButton:
            self.status = 2
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.status = 3
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
