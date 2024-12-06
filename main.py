import sys
import random
from UI import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class CircleDrawer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.draw_random_circle)

        self.circles = []

    def draw_random_circle(self):
        radius = random.randint(20, 100)
        x = random.randint(0, self.width() - radius * 2)
        y = random.randint(0, self.height() - radius * 2)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.circles.append((x, y, radius, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, radius, color in self.circles:
            painter.setBrush(color)
            painter.setPen(Qt.GlobalColor.transparent)
            painter.drawEllipse(x, y, radius * 2, radius * 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())