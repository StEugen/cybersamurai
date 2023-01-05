from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtWebEngineWidgets import *
import sys

class mainWindow(QMainWindow):
    """ Main window """
    def __init__(self):
        super(mainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(
            'https://www.google.com'
        ))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        home_btn = QAction('Home', self)

        self.addToolBar(navbar)
        navbar.addAction(back_btn)
        navbar.addAction(forward_btn)
        navbar.addAction(reload_btn)
        navbar.addAction(home_btn)
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.updateURL)

    def navigate_Home(self):
        self.browser.setUrl(QUrl('https://github.com/StEugen'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def updateURL(self, q):
        self.url_bar.setText(q.toString())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName('Test Browser')
    window = mainWindow()
    window.show()
    sys.exit(app.exec())