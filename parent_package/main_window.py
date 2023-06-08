from PyQt6.QtWidgets import QMainWindow

from parent_package.parent_widget import ParentClass


class MainWindowApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Avcı Milenium Falcon V.1.0')
        self._central_widget = ParentClass()
        self.setCentralWidget(self._central_widget)
        # cover the whole screen
        self.showMaximized()
        self.setStyleSheet("""
        QMainWindow {
            background-color: #111111;
        }
        QLabel {
            color: white;
        }
        QTextEdit {
            background-color: black;
            color: #4FCCFE;
            border: 1px solid black;
            border-radius: 5px;
        }
    
        
        """)



