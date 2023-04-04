#!/usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QSpinBox, QPushButton
from PyQt6.QtCore import QTimer, Qt
import sys


class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Timer')
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.timer_display = QLCDNumber()
        self.timer_display.setDigitCount(8)  # Set the number of digits to 8
        layout.addWidget(self.timer_display)
        timer_layout = QHBoxLayout()
        layout.addLayout(timer_layout)
        self.hours_spinbox = QSpinBox()
        self.hours_spinbox.setRange(0, 23)
        self.hours_spinbox.setFixedSize(70, 50)
        timer_layout.addWidget(self.hours_spinbox)
        timer_layout.addWidget(QLabel('часы'))
        self.minutes_spinbox = QSpinBox()
        self.minutes_spinbox.setRange(0, 59)
        self.minutes_spinbox.setFixedSize(70, 50)
        timer_layout.addWidget(self.minutes_spinbox)
        timer_layout.addWidget(QLabel('минуты'))
        self.seconds_spinbox = QSpinBox()
        self.seconds_spinbox.setRange(0, 59)
        self.seconds_spinbox.setFixedSize(70, 50)
        timer_layout.addWidget(self.seconds_spinbox)
        timer_layout.addWidget(QLabel('секунды'))
        start_button = QPushButton('Start')
        start_button.clicked.connect(self.start_timer)
        layout.addWidget(start_button)


    def start_timer(self):
        self.elapsed_time = 0
        self.total_seconds = self.hours_spinbox.value() * 3600 + \
                              self.minutes_spinbox.value() * 60 + \
                              self.seconds_spinbox.value()
        hours, remainder = divmod(self.total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        self.timer_display.display(time_str)
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start()


    def update_timer(self):
        self.elapsed_time += 1
        remaining_seconds = self.total_seconds - self.elapsed_time
        if remaining_seconds <= 0:
            self.timer.stop()
            self.timer_display.display('00:00:00')
            return
        hours, remainder = divmod(remaining_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

        self.timer_display.display(time_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer = Timer()
    timer.show()
    sys.exit(app.exec())


