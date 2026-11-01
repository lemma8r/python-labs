from .figure import Figure
from .color import Color

class Rectangle(Figure):
    def __init__(self, width: float, height: float, color: Color):
        self.width = width
        self.height = height
        self.color = color
        self._name = "Прямоугольник"

    def area(self) -> float:
        return self.width * self.height

    def get_name(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return "{} {} цвета, ширина: {}, высота: {}, площадь: {:.2f}".format(
            self.get_name(), self.color.color_name, self.width, self.height, self.area()
        )
