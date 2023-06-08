from PyQt6.QtCore import Qt, QRectF, QTimer
from PyQt6.QtWidgets import QGraphicsItem


class GaugeAltitudeLines(QGraphicsItem):
    # This class basically draws the lines for the altitude gauge
    def __init__(self, parent=None):
        super().__init__(parent)
        self.radius = 140
        # test timer to update altitude
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.altitude_increase)
        self.timer.start()

        self.altitude = 0

    def boundingRect(self):
        return QRectF(-self.radius, -self.radius, self.radius * 2, self.radius * 2)

    def paint(self, painter, option, widget):
        # Draw the lines horizontally starting from the top of the circle to the bottom
        painter.setPen(Qt.GlobalColor.green)
        painter.setBrush(Qt.BrushStyle.NoBrush)

        top_line_y = int(-self.radius)
        bottom_line_y = int(self.radius)

        # Calculate the y-coordinate for the middle line
        middle_line_y = int((top_line_y + bottom_line_y) / 2)

        # Draw the lines every 10 pixels
        for y in range(top_line_y, bottom_line_y, 20):

            if y % 2 == 0:
                painter.drawLine(-40, y, 40, y )
                # draw altitude text
                painter.drawText(50, y, str(self.altitude - (y * 0.1)))
            else:
                painter.drawLine(-20, y, 20, y)
                painter.drawText(50, y, str(self.altitude - (y * 0.1)))

            if y == middle_line_y: # draw the middle line thicker and in blue
                painter.setPen(Qt.GlobalColor.cyan)
                painter.drawLine(-40, y, 40, y)
                painter.drawText(50, y, str(self.altitude - (y * 0.1)))
                painter.setPen(Qt.GlobalColor.green)
                # draw the center point and horizon line of the plane


    def altitude_increase(self):
        alti = int(self.altitude) + 9
        self.altitude = alti
        self.update()











