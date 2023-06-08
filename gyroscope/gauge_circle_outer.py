from PyQt6.QtCore import QRectF, Qt, QPointF
from PyQt6.QtGui import QPainter, QPainterPath
from PyQt6.QtWidgets import QGraphicsItem


class OuterGaugeCircle(QGraphicsItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.radius = 175

    def boundingRect(self):
        return QRectF(-self.radius, -self.radius, self.radius * 2, self.radius * 2)

    def paint(self, painter: QPainter, option, widget):
        # Draw the circle empty and triangle top of the circle

        painter.setPen(Qt.GlobalColor.yellow)
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawEllipse(-self.radius, -self.radius, self.radius * 2, self.radius * 2)

        # Draw the arrow
        arrow_size = 10  # Adjust the size of the arrow as desired
        painter.setPen(Qt.GlobalColor.red)
        painter.setBrush(Qt.GlobalColor.red)

        arrow_head =  QPainterPath()
        arrow_head.moveTo(0, -self.radius)
        arrow_head.lineTo(-arrow_size, -self.radius + arrow_size)
        arrow_head.lineTo(arrow_size, -self.radius + arrow_size)
        arrow_head.lineTo(0, -self.radius)
        painter.drawPath(arrow_head)











