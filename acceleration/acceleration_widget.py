from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout, QLCDNumber, QHBoxLayout, \
    QGraphicsDropShadowEffect, QLabel


class AccelerationWidget(QWidget):
    # This class will have classic panel and also circular gauge of speed
    # and acceleration
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widget_label = QLabel('ACCELERATION')
        self.widget_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.live_preview_button = QPushButton('Stop Live Preview')
        self.error_simulation = QPushButton('Simulate Error')
        self.loginto_flight_records = QPushButton('Log into Flight Record')
        self.instrument_diagnostic = QPushButton('Instrument Diagnostic')
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.widget_label)
        self.digital_x_velocity_lcd = QLCDNumber()
        self.digital_y_velocity_lcd = QLCDNumber()
        self.digital_z_velocity_lcd = QLCDNumber()
        # set the number of digits to display
        self.digital_x_velocity_lcd.setDigitCount(8)
        self.digital_y_velocity_lcd.setDigitCount(8)
        self.digital_z_velocity_lcd.setDigitCount(8)


        self.init_panel()
        self.setLayout(self.layout)

    def init_panel(self):
        # create horizontal side by side and add display
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.digital_x_velocity_lcd)
        self.horizontal_layout.addWidget(self.digital_y_velocity_lcd)
        self.horizontal_layout.addWidget(self.digital_z_velocity_lcd)
        self.layout.addLayout(self.horizontal_layout)
        # set back color of the lcd
        self.digital_x_velocity_lcd.setStyleSheet("background-color: black; color: #40D0FB")
        self.digital_y_velocity_lcd.setStyleSheet("background-color: black")
        self.digital_z_velocity_lcd.setStyleSheet("background-color: black")
        # set the color of the digits
        self.digital_x_velocity_lcd.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)
        self.digital_y_velocity_lcd.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)
        self.digital_z_velocity_lcd.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)
        # cet value of the lcd
        self.digital_x_velocity_lcd.display("0.000000")
        self.digital_y_velocity_lcd.display("0.000000")
        self.digital_z_velocity_lcd.display("0.000000")

        # set background frame color
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#383838"))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        # add glow effect to the buttons
        self.live_preview_button.setGraphicsEffect(
            QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QColor("#40D0FB"))
        )
        self.error_simulation.setGraphicsEffect(
            QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QColor("#40D0FB"))
        )
        self.loginto_flight_records.setGraphicsEffect(
            QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QColor("#40D0FB"))
        )
        self.instrument_diagnostic.setGraphicsEffect(
            QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QColor("#40D0FB"))
        )


        self.setStyleSheet("""
                            QLineEdit {
                                background-color: #1F1F1F;
                                color : white;
                                border-radius: 5px;
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




        self.layout.addWidget(self.live_preview_button)
        self.layout.addWidget(self.error_simulation)
        self.layout.addWidget(self.loginto_flight_records)
        self.layout.addWidget(self.instrument_diagnostic)
        self.layout.addWidget(self.text_edit)




    def init_speed_gauge(self):
        pass
