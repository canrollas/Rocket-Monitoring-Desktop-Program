import math

from PyQt6.QtCore import QRectF, Qt, QTimer, QPoint
from PyQt6.QtGui import QPainter, QPen, QBrush, QPainterPath
from PyQt6.QtWidgets import QGraphicsItem


class GaugeCircle(QGraphicsItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.rotate_test)
        self.timer.start()
        self.radius = 150

    def rotate_test(self):
        # rotate every 1 second by 0.1 degrees
        self.setRotation(self.rotation() + 0.5)
        self.update()

    def boundingRect(self):
        return QRectF(-self.radius, -self.radius, self.radius * 2, self.radius * 2)

    def paint(self, painter: QPainter, option, widget):
        # Draw the circle
        path = QPainterPath()
        path.addEllipse(self.boundingRect())
        painter.setPen(QPen(Qt.GlobalColor.green, 3))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawPath(path)

        angles = range(0, 360, 30)

        # draw the lines on the edge of the circle
        painter.setPen(QPen(Qt.GlobalColor.green, 2))
        for angle in angles:
            painter.save()
            painter.rotate(angle)
            painter.drawLine(0, -self.radius, 0, -self.radius + 10)
            # draw the text
            painter.drawText(-10, -self.radius + 25, str(angle))
            painter.restore()
        # draw the center point and horizon line of the plane
        painter.setPen(QPen(Qt.GlobalColor.red, 3))
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawEllipse(-5, -5, 10, 10)
        painter.drawLine(-self.radius, 0, self.radius, 0)
        # make the line look like a plane by drawing a triangle and angled lines
        painter.setPen(QPen(Qt.GlobalColor.red, 2))
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawLine(0, 0, 0, 20)
        painter.drawLine(0, 0, -10, -10)
        painter.drawLine(0, 0, 10, -10)

        # draw line -10 y axis point to left radius point
        painter.drawLine(0, 20, -self.radius, 0)
        # draw line 10 y axis point to right radius point
        painter.drawLine(0, 20, self.radius, 0)
        # now fill it with a brush
        painter.setPen(Qt.GlobalColor.red)
        painter.setBrush(QBrush(Qt.GlobalColor.red, Qt.BrushStyle.SolidPattern))
        painter.drawPolygon(
            [QPoint(-10, -10), QPoint(0, 20), QPoint(10, -10)]
        )









    def update_gyro(self,gyro_x ):
        pass

    def update_altitude(self, alt):
        pass


