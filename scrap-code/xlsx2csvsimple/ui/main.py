import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox, QLabel, QLineEdit
import xlsx2csv
import subprocess
import os

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

        self.run_shell_script_button = QPushButton("Run PowerShell Script", self)
        self.run_shell_script_button.setGeometry(50, 180, 300, 30)
        self.run_shell_script_button.clicked.connect(self.shell_script)

        self.group_label = QLabel("Group:", self)
        self.group_label.setGeometry(50, 100, 60, 30)
        self.group_input = QLineEdit(self)
        self.group_input.setGeometry(120, 100, 150, 30)

        self.faculty_label = QLabel("Faculty:", self)
        self.faculty_label.setGeometry(50, 140, 60, 30)
        self.faculty_input = QLineEdit(self)
        self.faculty_input.setGeometry(120, 140, 150, 30)

        self.file_label = QLabel("Selected File: ", self)
        self.file_label.setGeometry(50, 20, 300, 20)


    def select_file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Excel Files (*.xlsx);;All Files (*)")
        file_dialog.setViewMode(QFileDialog.ViewMode.List)

        if file_dialog.exec():
            file_name = file_dialog.selectedFiles()[0]
            self.selected_file_path = file_name
            file_name_only = os.path.basename(file_name)
            self.file_label.setText(f"Selected File: {file_name_only}")


    def run_script(self):
        if self.selected_file_path:
            try:
                xlsx2csv.convert_excel_to_csv(self.selected_file_path)
                self.file_label.clear()  # Clear the label when conversion is successful
                QMessageBox.information(self, "Success", "Conversion completed.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
        else:
            QMessageBox.warning(self, "Warning", "Please select an Excel file first.")


    def shell_script(self):
        if self.selected_file_path:
            group = self.group_input.text()
            faculty = self.faculty_input.text()

            if group and faculty:
                script_template = '''
'''

                script_file_path = "script.ps1"
                with open(script_file_path, "w") as script_file:
                    script_file.write(script_template.format(group=group, faculty=faculty))

                subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_file_path])


                os.remove(script_file_path)
            else:
                QMessageBox.warning(self, "Warning", "Please enter both group and faculty.")
        else:
            QMessageBox.warning(self, "Warning", "Please select an Excel file first.")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
