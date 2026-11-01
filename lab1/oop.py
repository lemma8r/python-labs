"""
Лабораторная работа №1. Биквадратное уравнение.
Объектно-ориентированная парадигма: решение через классы.

Уравнение: a*x^4 + b*x^2 + c = 0
Замена:    y = x^2, y >= 0
"""

import sys
import math


class CoefficientReader:
    """Класс для чтения коэффициентов из argv или с клавиатуры."""

    def __init__(self, argv):
        self.argv = argv

    def read(self, index, prompt):
        """
        Читаем коэффициент из командной строки или вводим с клавиатуры.
        Повторяем ввод, пока не получим корректное число.
        """
        coef_str = None
        if len(self.argv) > index:
            coef_str = self.argv[index]

        while True:
            if coef_str is None:
                print(prompt)
                coef_str = input()
            try:
                return float(coef_str)
            except ValueError:
                print(f"Некорректное значение: '{coef_str}'. Введите число заново.")
                coef_str = None


class BiquadraticEquation:
    """Биквадратное уравнение a*x^4 + b*x^2 + c = 0."""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        """Дискриминант квадратного уравнения относительно y = x^2."""
        return self.b * self.b - 4 * self.a * self.c

    def solve(self):
        """
        Возвращает список действительных корней биквадратного уравнения.
        """
        roots = []

        if self.a == 0:
            # Вырожденный случай: b*x^2 + c = 0
            if self.b == 0:
                return roots
            y = -self.c / self.b
            return self._roots_from_y(y)

        D = self.discriminant()

        if D < 0:
            return roots
        if D == 0:
            y = -self.b / (2 * self.a)
            return self._roots_from_y(y)

        sqD = math.sqrt(D)
        y1 = (-self.b + sqD) / (2 * self.a)
        y2 = (-self.b - sqD) / (2 * self.a)
        roots.extend(self._roots_from_y(y1))
        roots.extend(self._roots_from_y(y2))
        return roots

    @staticmethod
    def _roots_from_y(y):
        """Из значения y = x^2 получаем корни x."""
        if y > 0:
            sq = math.sqrt(y)
            return [sq, -sq]
        if y == 0:
            return [0.0]
        return []

    def __str__(self):
        return f"{self.a}*x^4 + {self.b}*x^2 + {self.c} = 0"


class RootsPrinter:
    """Класс для красивого вывода корней."""

    @staticmethod
    def print(roots):
        n = len(roots)
        if n == 0:
            print("Нет действительных корней")
        elif n == 1:
            print(f"Один корень: {roots[0]}")
        elif n == 2:
            print(f"Два корня: {roots[0]} и {roots[1]}")
        elif n == 3:
            print(f"Три корня: {roots[0]}, {roots[1]} и {roots[2]}")
        else:
            print(f"Четыре корня: {roots[0]}, {roots[1]}, {roots[2]} и {roots[3]}")


def main():
    reader = CoefficientReader(sys.argv)
    a = reader.read(1, "Введите коэффициент А:")
    b = reader.read(2, "Введите коэффициент B:")
    c = reader.read(3, "Введите коэффициент C:")

    equation = BiquadraticEquation(a, b, c)
    print(f"Уравнение: {equation}")

    roots = equation.solve()
    RootsPrinter.print(roots)


if __name__ == "__main__":
    main()
