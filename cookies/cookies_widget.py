from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QGraphicsDropShadowEffect


class CookiesWidget(QWidget):
    def __init__(self):
        super().__init__()
        # FIXME icons must be implemented
        self.icon_heat = None
        self.icon_pressure = None
        self.icon_time = None
        self.icon_humidity = None
        self.heat_button = QPushButton('220 C')
        self.pressure_button = QPushButton('63.5 psi')
        self.time_button = QPushButton('10:40 PM')
        self.humidity_button = QPushButton('Humidity')
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.init_panel()
        # set background frame color
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#383838"))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setStyleSheet("""
              
                

                QPushButton {
                                background-color: #40D0FB;
                                color : black;
                                border-radius: 5px;
                                height: 30px;
                                min-width: 125px;
                            }
  
                """)

    def init_panel(self):
        self.grid_layout.addWidget(self.heat_button, 0, 0)
        self.grid_layout.addWidget(self.pressure_button, 0, 1)
        self.grid_layout.addWidget(self.time_button, 1, 0)
        self.grid_layout.addWidget(self.humidity_button, 1, 1)



