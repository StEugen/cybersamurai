import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Upload Application")
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: #454545;")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        central_widget.setLayout(layout)

        upload_button = QPushButton("Upload")
        upload_button.setStyleSheet(
            """
            QPushButton {
                background-color: green;
                color: white;
                border-radius: 10px;
                font-size: 20px;
                padding: 10px;
            }

            QPushButton:hover {
                background-color: lightgreen;
            }
            """
        )
        upload_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        upload_button.clicked.connect(self.select_file)
        layout.addWidget(upload_button)

    def select_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.jpeg *.bmp)")
        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            selected_files = file_dialog.selectedFiles()
            print("Selected file(s):", selected_files)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
