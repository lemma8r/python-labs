import math
from .figure import Figure
from .color import Color

class Circle(Figure):
    def __init__(self, radius: float, color: Color):
        self.radius = radius
        self.color = color
        self._name = "Круг"

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def get_name(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return "{} {} цвета, радиус: {}, площадь: {:.2f}".format(
            self.get_name(), self.color.color_name, self.radius, self.area()
        )
