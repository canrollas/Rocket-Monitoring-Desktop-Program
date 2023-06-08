from PyQt6.QtGui import QColor, QPalette, QPixmap
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from acceleration.acceleration_widget import AccelerationWidget
from angle.angle_widget import AngleWidget
from cookies.cookies_widget import CookiesWidget
from gyroscope.gauge_parent_widget import GaugeWidgetParent
from ignition.ignition_widget import IgnitionWidget
from location.location_widget import LocationWidget


class ParentClass(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        widget_container_palette = QPalette()
        widget_container_palette.setColor(QPalette.ColorRole.Window, QColor("#1D1F1E"))

        self.parent = parent
        self.horizontal_layout = QHBoxLayout()
        self.col_1 = QVBoxLayout()
        self.col_2 = QVBoxLayout()
        self.col_3 = QVBoxLayout()

        self.setLayout(self.horizontal_layout)

        # call first gyro widget
        self.container_gyro = QWidget()
        self.container_gyro.setAutoFillBackground(True)
        self.container_gyro.setPalette(widget_container_palette)
        container_gyro = QVBoxLayout()
        self.container_gyro.setLayout(container_gyro)

        self.gyro_widget = GaugeWidgetParent()
        container_gyro.addWidget(self.gyro_widget)
        self.col_1.addWidget(self.container_gyro)
        # call the cookie, ignition and acceleration widget in same column
        self.container_cookies = QWidget()
        self.container_cookies.setAutoFillBackground(True)
        self.container_cookies.setPalette(widget_container_palette)
        container_cookies = QVBoxLayout()
        self.container_cookies.setLayout(container_cookies)
        self.container_ignition = QWidget()
        self.container_ignition.setAutoFillBackground(True)
        self.container_ignition.setPalette(widget_container_palette)
        container_ignition = QVBoxLayout()
        self.container_ignition.setLayout(container_ignition)
        self.container_acceleration = QWidget()
        self.container_acceleration.setAutoFillBackground(True)
        self.container_acceleration.setPalette(widget_container_palette)
        container_acceleration = QVBoxLayout()
        self.container_acceleration.setLayout(container_acceleration)


        self.cookie_widget = CookiesWidget()
        self.ignition_widget = IgnitionWidget()
        self.acceleration_widget = AccelerationWidget()
        container_cookies.addWidget(self.cookie_widget)
        container_ignition.addWidget(self.ignition_widget)
        container_acceleration.addWidget(self.acceleration_widget)

        self.col_2.addWidget(self.container_cookies)
        self.col_2.addWidget(self.container_ignition)
        self.col_2.addWidget(self.container_acceleration)

        # call the angle widget and location widget in same column
        self.container_widget_angle = QWidget()
        self.container_widget_angle.setAutoFillBackground(True)
        self.container_widget_angle.setPalette(widget_container_palette)
        container_inner_layout = QVBoxLayout()
        self.container_widget_angle.setLayout(container_inner_layout)
        self.angle_widget = AngleWidget()
        container_inner_layout.addWidget(self.angle_widget)

        self.container_widget_loc = QWidget()
        self.container_widget_loc.setAutoFillBackground(True)
        self.container_widget_loc.setPalette(widget_container_palette)
        self.location_widget = LocationWidget()
        container_inner_layout = QVBoxLayout()
        self.container_widget_loc.setLayout(container_inner_layout)
        container_inner_layout.addWidget(self.location_widget)



        self.col_3.addWidget(self.container_widget_angle)

        self.col_3.addWidget(self.container_widget_loc)

        self.horizontal_layout.addLayout(self.col_1)
        self.horizontal_layout.addLayout(self.col_2)
        self.horizontal_layout.addLayout(self.col_3)


        self.horizontal_layout.setStretch(0, 2)
        self.horizontal_layout.setStretch(1, 1)
        # make the third column smaller
        self.horizontal_layout.setStretch(2, 2)




