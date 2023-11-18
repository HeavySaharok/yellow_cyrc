import random
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.coords = (100, 100)
        self.pushButton.clicked.connect(self.click)

    def draw(self, qp):
        r = random.randint(20, 100)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(int(self.coords[0] - r / 2), int(self.coords[1] - r / 2), r, r)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def click(self):
        self.coords = (random.randint(20, self.width() - 20), random.randint(20, self.height() - 20))
        self.do_paint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
