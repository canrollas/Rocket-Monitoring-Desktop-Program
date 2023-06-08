from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsTextItem

from gyroscope.gauge_altitude_lines import GaugeAltitudeLines
from gyroscope.gauge_circle import GaugeCircle
from gyroscope.gauge_circle_outer import OuterGaugeCircle


class GaugeScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSceneRect(0, 0, 520, 500)
        self.setBackgroundBrush(Qt.GlobalColor.black)
        self.gauge_lines = GaugeAltitudeLines()
        self.gauge = GaugeCircle()
        # center the gauge
        self.outer_gauge = OuterGaugeCircle()
        self.gauge.setPos(300, 300)
        self.outer_gauge.setPos(300, 300)
        self.gauge_lines.setPos(300, 300)
        self.addItem(self.gauge)
        self.addItem(self.outer_gauge)
        self.addItem(self.gauge_lines)
        self.gyro_x_graphic = QGraphicsTextItem("G-X: 0")
        self.gyro_y_graphic =  QGraphicsTextItem("G-Y: 0")
        self.gyro_z_graphic =  QGraphicsTextItem("G-Z: 0")
        self.altitude_graphic =  QGraphicsTextItem("Altitude: 0")
        self.relative_altitude_graphic =  QGraphicsTextItem("R.Altitude: 0")
        self.sea_level_altitude_graphic = QGraphicsTextItem("S.L.Altitude: 0")
        # add bottom on the scene horizontally
        self.gyro_x_graphic.setPos(180, 475)
        self.gyro_y_graphic.setPos(280, 475)
        self.gyro_z_graphic.setPos(380, 475)
        self.altitude_graphic.setPos(180, 25)
        self.relative_altitude_graphic.setPos(280, 25)
        self.sea_level_altitude_graphic.setPos(380, 25)

        # set color to white
        self.gyro_x_graphic.setDefaultTextColor(Qt.GlobalColor.white)
        self.gyro_y_graphic.setDefaultTextColor(Qt.GlobalColor.white)
        self.gyro_z_graphic.setDefaultTextColor(Qt.GlobalColor.white)
        self.altitude_graphic.setDefaultTextColor(Qt.GlobalColor.white)
        self.relative_altitude_graphic.setDefaultTextColor(Qt.GlobalColor.white)
        self.sea_level_altitude_graphic.setDefaultTextColor(Qt.GlobalColor.white)

        self.addItem(self.gyro_x_graphic)
        self.addItem(self.gyro_y_graphic)
        self.addItem(self.gyro_z_graphic)
        self.addItem(self.altitude_graphic)
        self.addItem(self.relative_altitude_graphic)
        self.addItem(self.sea_level_altitude_graphic)
        #make it scrollable
        self.setStickyFocus(True)





    def update_gyroxyz(self, x, y, z):
        #self.gauge.update_gyroxyz(x, y, z)
        pass
    def update_altitude(self, alt):
        #self.gauge.update_altitude(alt)
        pass
    def update_relative_altitude(self, relative_alt):
        #self.gauge.update_relative_altitude(relative_alt)
        pass
    def update_sea_level_altitude(self, sea_level_alt):
        #self.gauge.update_sea_level_altitude(sea_level_alt)
        pass