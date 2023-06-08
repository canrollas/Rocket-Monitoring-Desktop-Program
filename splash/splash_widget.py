from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QWidget, QProgressBar

from parent_package.main_window import MainWindowApplication


class SplashScreenWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(450, 450)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.WindowType.Tool)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("/Users/canrollas/PycharmProjects/qt_application/splash_back.png"))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.label.setFixedSize(450, 450)
        self.progress_bar = QProgressBar(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.timer.start(100)
        self.counter = 0

        self.progress_bar.setFixedSize(300, 20)
        self.progress_bar.setStyleSheet("""
        QProgressBar {
            border: 2px solid grey;
            border-radius: 5px;
            text-align: center;
        }
        QProgressBar::chunk {
            background-color: #40D0FB;
            width: 10px;
        }
        """)
        self.progress_bar.move(75, 350)
        self.label.move(0, 0)

    def progress(self):

        self.progress_bar.setValue(self.counter)
        self.counter += 1
        if self.counter > 100:
            self.timer.stop()
            self.main_window = MainWindowApplication()
            self.main_window.show()
            self.close()
