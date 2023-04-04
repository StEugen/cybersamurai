import sys
from PyQt6.QtCore import QTimer, QTime, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Clock')

        self.time_label = QLabel(self)
        font = QFont('Arial', 250, QFont.Weight.Bold)
        self.time_label.setFont(font)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.exit_button = QPushButton('Exit', self)
        self.exit_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        layout.addWidget(self.exit_button)


        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def resizeEvent(self, event):
        self.time_label.setGeometry(0, 0, self.width(), self.height())

    def update_time(self):
        current_time = QTime.currentTime()
        time_string = current_time.toString('hh:mm:ss')
        self.time_label.setText(time_string)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Clock()
    clock.showFullScreen()
    sys.exit(app.exec())




