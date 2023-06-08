from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QTextEdit, QGraphicsDropShadowEffect, QLabel
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
import folium
import io


class LocationWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Create the inner frame widget
        self.frame = QWidget(self)
        self.rocket_location = QLabel('ROCKET LOCATION')



        self.rocket_location.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.window_width, self.window_height = 300, 150
        self.setMinimumSize(self.window_width, self.window_height)

        self.live_preview_button = QPushButton('Stop Live Preview')
        self.error_simulator_button = QPushButton('Simulate Error')
        self.log_into_flight_record = QPushButton('Log Flight Record')
        self.instrument_diagnostic = QPushButton('Instr Diagnostic')
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.coordinate = (37.8199286, 27.4782551)
        self.m = folium.Map(
            location=self.coordinate,
            tiles='Stamen Terrain',  # Change the tile provider and style
            # dark mode
            zoom_start=13,
            prefer_canvas=True
        )





        self.red_marker = folium.Marker(
            location=self.coordinate,
            popup='Rocket Location',
            icon=folium.Icon(color='red'),
            id = 'marker'



        )

        self.m.add_child(self.red_marker)

        # Save map data to data object
        data = io.BytesIO()
        self.m.save(data, close_file=False)

        self.webView = QWebEngineView()
        self.webView.setHtml(data.getvalue().decode())
        self.layout.addWidget(self.rocket_location)
        self.layout.addWidget(self.webView)
        self.init_panel()

        # Create a QTimer to update marker position
        self.timer = QTimer()
        self.timer.setInterval(1000)  # Update every 1 second
        self.timer.timeout.connect(self.update_coordinates)
        self.timer.start()

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

    def init_panel(self):
        local_vertical = QVBoxLayout()

        local_vertical.addWidget(self.live_preview_button)
        local_vertical.addWidget(self.error_simulator_button)
        local_vertical.addWidget(self.log_into_flight_record)
        local_vertical.addWidget(self.instrument_diagnostic)
        local_horizontal = QHBoxLayout()
        local_horizontal.addLayout(local_vertical)
        local_horizontal.addWidget(self.text_edit)
        self.layout.addLayout(local_horizontal)
        # add gloving effect background color of #40D0FB

        # set only button has gloving effect
        self.live_preview_button.setGraphicsEffect(
            QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QColor("#40D0FB"))
        )
        self.error_simulator_button.setGraphicsEffect(
            QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QColor("#40D0FB"))
        )
        self.log_into_flight_record.setGraphicsEffect(
            QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QColor("#40D0FB"))
        )
        self.instrument_diagnostic.setGraphicsEffect(
            QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QColor("#40D0FB"))
        )

    def update_coordinates(self):
        # Update coordinates every call
        self.coordinate = (self.coordinate[0] + 0.03, self.coordinate[1] + 0.03)
        self.red_marker.location = self.coordinate
        # Save map data to data object
        self.m.location = self.coordinate
        # add coordinates legend to map
        self.m.add_child(folium.LatLngPopup())
        data = io.BytesIO()
        self.m.save(data, close_file=False)
        self.webView.setHtml(data.getvalue().decode())

        # Push text to text edit
        self.text_edit.append(f'Rocket Location: {self.coordinate}')




