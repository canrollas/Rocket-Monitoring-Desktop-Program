from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QGraphicsView

from gyroscope.gauge_scene import GaugeScene


class GaugeGraphicView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)

        self.scene = GaugeScene()
        self.setScene(self.scene)

    def update_gyroxyz(self, x, y, z):
        pass
    def update_altitude(self, alt):
        pass
    def update_relative_altitude(self, relative_alt):
        pass

    def update_sea_level_altitude(self, sea_level_alt):
        pass
