import os
import sys
import io
import folium  # pip install folium
from PyQt6.QtCore import QTimer, QUrl
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt6.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine

from PyQt6.QtSensors import QGyroscope

"""
Folium in PyQt5
"""

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
import folium
import io


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Leaflet in PyQt Example')
        self.window_width, self.window_height = 800, 600
        self.setMinimumSize(self.window_width, self.window_height)

        self.live_preview_button = QPushButton('Stop Live Preview')
        self.error_simulator_button = QPushButton('Simulate Error')
        self.log_into_flight_record = QPushButton('Log into Flight Record')
        self.instrument_diagnostic = QPushButton('Instrument Diagnostic')
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.coordinate = (37.8199286, 27.4782551)
        self.m = folium.Map(
            location=self.coordinate,
            # dark mode
            zoom_start=13,
            prefer_canvas=True
        )

        self.red_marker = folium.Marker(
            location=self.coordinate,
            popup='Red Marker',
            icon=folium.Icon(color='red')
        )
        self.m.add_child(self.red_marker)

        # Save map data to data object
        data = io.BytesIO()
        self.m.save(data, close_file=False)

        self.webView = QWebEngineView()
        self.webView.setHtml(data.getvalue().decode())
        self.layout.addWidget(self.webView)
        self.init_panel()

        # Create a QTimer to update marker position
        self.timer = QTimer()
        self.timer.setInterval(1000)  # Update every 1 second
        self.timer.timeout.connect(self.update_marker_position)
        self.timer.start()

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


    def update_marker_position(self):
        # Update marker position
        new_coordinate = (self.coordinate[0] + 0.001, self.coordinate[1] + 0.001)
        self.red_marker.location = new_coordinate
        self.coordinate = new_coordinate

        # Save updated map data to data object
        data = io.BytesIO()
        self.m.save(data, close_file=False)

        # Reload the map by setting the updated HTML content
        self.webView.setHtml(data.getvalue().decode())



    def set_coordinate(self, lat, lng):
        self.coordinate = (lat, lng)
        self.m = folium.Map(
            location=self.coordinate,
            # dark mode
            zoom_start=13,
            prefer_canvas=True
        )

        self.red_marker = folium.Marker(
            location=self.coordinate,
            popup='Red Marker',
            icon=folium.Icon(color='red')
        )
        self.m.add_child(self.red_marker)

        # Save map data to data object
        data = io.BytesIO()
        self.m.save(data, close_file=False)

        self.webView.setHtml(data.getvalue().decode())



