from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QPushButton, QLineEdit, QLabel, QWidget, QGridLayout, QGraphicsDropShadowEffect, QHBoxLayout


class AngleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.widget_label = QLabel('ROCKET ANGLE')
        self.widget_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.angle_x_label = QLabel('Angle X')
        self.angle_y_label = QLabel('Angle Y')
        self.angle_z_label = QLabel('Angle Z')
        self.error_indicator_label = QLabel('Error Indicator')

        self.angle_x_line_edit = QLineEdit("0")
        self.angle_y_line_edit = QLineEdit("0")
        self.angle_z_line_edit = QLineEdit("0")
        self.error_line_edit = QLineEdit("No Error")
        self.error_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # set read only
        self.angle_x_line_edit.setReadOnly(True)
        self.angle_y_line_edit.setReadOnly(True)
        self.angle_z_line_edit.setReadOnly(True)
        self.error_line_edit.setReadOnly(True)

        # Three buttons
        self.error_sim_button = QPushButton('Simulate Error')
        self.log_into_flight_records = QPushButton('Log Flight Record')
        self.live_preview_button = QPushButton('Stop Live Preview')
        self.error_sim_button.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QColor("#40D0FB")))
        self.log_into_flight_records.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QColor("#40D0FB")))
        self.live_preview_button.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QColor("#40D0FB")))


        # Angle label-x : x value, Angle label-y : y value, Angle label-z : z value Error indicator : No Error
        # Three buttons will be under the three labels
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # set background frame color
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#383838"))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setStyleSheet("""
        QLineEdit {
                        background-color: #1F1F1F;
                        color : white;
                        border-radius: 5px;
                        height: 30px;
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
        # insert the labels and buttons into the layout
        # insert widget label
        self.layout.addWidget(self.widget_label, 0, 0, 1, 8)
        local_horizontal = QHBoxLayout()
        local_horizontal.addWidget(self.angle_x_label)
        local_horizontal.addWidget(self.angle_x_line_edit)
        local_horizontal.addWidget(self.angle_y_label)
        local_horizontal.addWidget(self.angle_y_line_edit)
        local_horizontal.addWidget(self.angle_z_label)
        local_horizontal.addWidget(self.angle_z_line_edit)

        self.layout.addLayout(local_horizontal, 1, 0, 1, 8)
        self.layout.addWidget(self.error_indicator_label, 2, 0)
        self.layout.addWidget(self.error_line_edit, 2, 1, 1, 7)

        # Three buttons will be under the three labels and first row length must be sliced to 3 columns
        self.layout.addWidget(self.error_sim_button,3, 0, 1, 3)
        self.layout.addWidget(self.log_into_flight_records, 3, 3, 1, 3)
        self.layout.addWidget(self.live_preview_button, 3, 6, 1, 2)





