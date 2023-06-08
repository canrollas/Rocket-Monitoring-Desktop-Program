from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QGraphicsDropShadowEffect


class IgnitionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.first_ignition_label = QLabel('First Ignition')
        self.second_ignition_label = QLabel('Second Ignition')
        self.first_ignition_line_edit = QLineEdit("Not Executed")
        self.second_ignition_line_edit = QLineEdit("Not Executed")
        self.error_label = QLabel('Error Indicator')
        self.error_line_edit = QLineEdit("No Error")
        self.error_line_edit.setReadOnly(True)
        self.first_ignition_line_edit.setReadOnly(True)
        self.second_ignition_line_edit.setReadOnly(True)
        self.error_sim_button = QPushButton('Simulate Error')
        self.emergency_stop_button = QPushButton('Emergency Stop')
        self.error_sim_button.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QColor("#40D0FB")))
        self.emergency_stop_button.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QColor("#40D0FB")))
        # set background frame color
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#383838"))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        self.widget_label = QLabel('IGNITION')
        self.widget_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setStyleSheet("""
        QLineEdit {
                        background-color: #1F1F1F;
                        color : white;
                        border-radius: 5px;
                        height: 30px;
                        min-width: 125px;
                    }
                    QPushButton {
                        background-color: #1F1F1F;
                        color : white;
                        border-radius: 5px;
                        height: 30px;
                        min-width: 125px;
                    }
                    QPushButton:hover {
                        background-color: #40D0FB;
                        color : black;
                    }
                    QPushButton:pressed {
                        background-color: white;
                        color : black;
                    }
        """)
        self.init_panel()

    def init_panel(self):
        self.layout.addWidget(self.widget_label, 0, 0, 1, 2)
        self.layout.addWidget(self.first_ignition_label, 1, 0)
        self.layout.addWidget(self.first_ignition_line_edit, 1, 1)
        self.layout.addWidget(self.second_ignition_label, 2, 0)
        self.layout.addWidget(self.second_ignition_line_edit, 2, 1)
        self.layout.addWidget(self.error_label, 3, 0)
        self.layout.addWidget(self.error_line_edit, 3, 1)
        self.layout.addWidget(self.error_sim_button, 4, 0)
        self.layout.addWidget(self.emergency_stop_button, 4, 1)



