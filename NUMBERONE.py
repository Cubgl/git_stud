import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 400, 400)
        self.setWindowTitle('Координаты')
        self.x = 0
        self.y = 0

        self.pixmap = QPixmap('alien.png')
        self.image = QLabel(self)
        self.image.move(0, 0)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)
        self.setMouseTracking(True)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.y -= 5
            self.image.move(self.x, self.y)
        elif event.key() == Qt.Key_Down:
            self.y += 5
            self.image.move(self.x, self.y)
        elif event.key() == Qt.Key_Right:
            self.x += 5
            self.image.move(self.x, self.y)
        elif event.key() == Qt.Key_Left:
            self.x -= 5
            self.image.move(self.x, self.y)
        if self.x > 350:
            self.x = 0
            self.image.move(self.x, self.y)
        elif self.x < 0:
            self.x = 350
            self.image.move(self.x, self.y)
        if self.y > 350:
            self.y = 0
            self.image.move(self.x, self.y)
        elif self.y < 0:
            self.y = 350
            self.image.move(self.x, self.y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
