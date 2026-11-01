import unittest
import math
from lab_python_oop.color import Color
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
from lab_python_oop.circle import Circle

class TestGeometricFigures(unittest.TestCase):

    def test_rectangle_area(self):
        rect = Rectangle(3, 4, Color("синего"))
        self.assertEqual(rect.area(), 12)
        self.assertEqual(rect.get_name(), "Прямоугольник")

    def test_square_area(self):
        square = Square(5, Color("красного"))
        self.assertEqual(square.area(), 25)
        self.assertEqual(square.get_name(), "Квадрат")
        # Проверяем, что квадрат унаследовался от прямоугольника
        self.assertIsInstance(square, Rectangle)

    def test_circle_area(self):
        circle = Circle(2, Color("зеленого"))
        # Площадь круга = pi * r^2. Проверяем с точностью до 2 знаков
        self.assertAlmostEqual(circle.area(), math.pi * 4, places=2)
        self.assertEqual(circle.get_name(), "Круг")

if __name__ == '__main__':
    unittest.main()
