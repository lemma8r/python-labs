"""
Лабораторная работа №5. Модульное тестирование.
Модифицированный код из ЛР №1 (биквадратное уравнение).

Уравнение: a*x^4 + b*x^2 + c = 0
Замена:    y = x^2, y >= 0

Код подготовлен к тестированию:
- solve_biquadratic() — чистая функция без I/O;
- get_coef() принимает argv и input_func, что позволяет
  подменять зависимости в тестах (инъекция зависимостей и Mock).
"""

import math
import sys


def solve_biquadratic(a, b, c):
    """
    Решение биквадратного уравнения a*x^4 + b*x^2 + c = 0.

    Returns:
        list[float]: список действительных корней (может быть пустым)
    """
    roots = []

    # Вырожденный случай: a == 0 -> b*x^2 + c = 0
    if a == 0:
        if b == 0:
            return roots
        y = -c / b
        return roots_from_y(y)

    D = b * b - 4 * a * c

    if D < 0:
        return roots

    if D == 0:
        y = -b / (2 * a)
        return roots_from_y(y)

    sqD = math.sqrt(D)
    y1 = (-b + sqD) / (2 * a)
    y2 = (-b - sqD) / (2 * a)
    roots.extend(roots_from_y(y1))
    roots.extend(roots_from_y(y2))
    return roots


def roots_from_y(y):
    """Из значения y = x^2 получаем корни x."""
    if y > 0:
        sq = math.sqrt(y)
        return [sq, -sq]
    if y == 0:
        return [0.0]
    return []


def get_coef(index, prompt, argv=None, input_func=input):
    """
    Читаем коэффициент из командной строки или вводим с клавиатуры.
    Повторяем ввод, пока не получим корректное число.

    Args:
        index (int): номер параметра в командной строке
        prompt (str): приглашение для ввода
        argv (list | None): список аргументов командной строки
                            (по умолчанию sys.argv)
        input_func (callable): функция ввода (по умолчанию input),
                               нужна для подмены в тестах

    Returns:
        float: коэффициент уравнения
    """
    if argv is None:
        argv = sys.argv

    coef_str = argv[index] if len(argv) > index else None

    while True:
        if coef_str is None:
            print(prompt)
            coef_str = input_func()
        try:
            return float(coef_str)
        except ValueError:
            print(f"Некорректное значение: '{coef_str}'. Введите число заново.")
            coef_str = None


def print_roots(roots):
    """Красивый вывод корней."""
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
    a = get_coef(1, "Введите коэффициент А:")
    b = get_coef(2, "Введите коэффициент B:")
    c = get_coef(3, "Введите коэффициент C:")

    roots = solve_biquadratic(a, b, c)
    print_roots(roots)


if __name__ == "__main__":
    main()
