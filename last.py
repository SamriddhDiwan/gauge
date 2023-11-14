import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 200, 200)

        # Code for gauge
        self.gauge_label = QLabel(self)
        self.gauge_label.setPixmap(QPixmap("meter.png"))
        self.gauge_label.setGeometry(-50, 0, 200, 200)

        # Code for pointer
        self.indicator_label = QLabel(self)
        self.indicator_label.setPixmap(QPixmap("triangle.png"))
        self.indicator_label.setGeometry(35, 125, 37, 20)  

    def indicator_percentage(self, percentage):
        window_height = self.height()
        y_position = int((percentage / 100) * window_height)
        
        x_gauge, y_gauge, _, _ = self.gauge_label.geometry().getRect()
        
        self.indicator_label.setGeometry(x_gauge + 35, y_gauge + 125 - y_position, 37, y_position + 20)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageWindow()
    window.show()

    sys.exit(app.exec_())
