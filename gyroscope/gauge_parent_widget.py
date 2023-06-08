from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QGraphicsDropShadowEffect

from gyroscope.gauge_view import GaugeGraphicView


class GaugeWidgetParent(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.gauge_view = GaugeGraphicView()
        self.live_preview_button = QPushButton('Stop Live Preview')
        self.error_simulation = QPushButton('Simulate Error')
        self.loginto_flight_records = QPushButton('Log into Flight Record')
        self.instrument_diagnostic = QPushButton('Instrument Diagnostic')
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.layout = QVBoxLayout()


        self.init_panel()

    def init_panel(self):
        local_vertical = QVBoxLayout()
        local_vertical.addWidget(self.live_preview_button)
        local_vertical.addWidget(self.error_simulation)
        local_vertical.addWidget(self.loginto_flight_records)
        local_vertical.addWidget(self.instrument_diagnostic)
        # set background frame color
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#383838"))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        # set only button has gloving effect
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

        local_horizontal = QHBoxLayout()
        local_horizontal.addLayout(local_vertical)
        local_horizontal.addWidget(self.text_edit)
        self.layout.addWidget(self.gauge_view)
        self.layout.addLayout(local_horizontal)
        self.setLayout(self.layout)









