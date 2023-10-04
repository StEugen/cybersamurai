import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox
import xlsx2csv

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Excel to CSV Converter")
        self.setGeometry(100, 100, 400, 200)

        self.select_file_button = QPushButton("Select Excel File", self)
        self.select_file_button.setGeometry(50, 50, 150, 30)
        self.select_file_button.clicked.connect(self.select_file)

        self.run_script_button = QPushButton("Convert", self)
        self.run_script_button.setGeometry(200, 50, 150, 30)
        self.run_script_button.clicked.connect(self.run_script)

        self.selected_file_path = None

    def select_file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Excel Files (*.xlsx);;All Files (*)")
        file_dialog.setViewMode(QFileDialog.ViewMode.List)

        if file_dialog.exec():
            file_name = file_dialog.selectedFiles()[0]
            self.selected_file_path = file_name

    def run_script(self):
        if self.selected_file_path:
            try:
                xlsx2csv.convert_excel_to_csv(self.selected_file_path)
                QMessageBox.information(self, "Success", "Conversion completed.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
        else:
            QMessageBox.warning(self, "Warning", "Please select an Excel file first.")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
