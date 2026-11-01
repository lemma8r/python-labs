from lab_python_oop.color import Color
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
from lab_python_oop.circle import Circle

from prettytable import PrettyTable

def main():
    N = 1  # номер варианта

    # Создаем объекты
    rect = Rectangle(N, N, Color("синего"))
    circle = Circle(N, Color("зеленого"))
    square = Square(N, Color("красного"))

    # Выводим через repr (как требует задание)
    print("Вывод через repr():")
    print(rect)
    print(circle)
    print(square)

    # Вывод с использованием внешнего пакета prettytable
    print("\nВывод с использованием внешнего пакета prettytable:")
    table = PrettyTable()
    table.field_names = ["Фигура", "Цвет", "Размеры", "Площадь"]

    table.add_row([rect.get_name(), rect.color.color_name, f"{rect.width}x{rect.height}", f"{rect.area():.2f}"])
    table.add_row([circle.get_name(), circle.color.color_name, f"R={circle.radius}", f"{circle.area():.2f}"])
    table.add_row([square.get_name(), square.color.color_name, f"{square.width}x{square.height}", f"{square.area():.2f}"])

    print(table)

if __name__ == "__main__":
    main()
