"""
Лабораторная работа №1. Биквадратное уравнение.
Процедурная парадигма: решение через функции (def).

Уравнение: a*x^4 + b*x^2 + c = 0
Замена:    y = x^2, y >= 0
"""

import sys
import math


def get_coef(index, prompt):
    """
    Читаем коэффициент из командной строки или вводим с клавиатуры.
    Повторяем ввод, пока не получим корректное число.

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффициента

    Returns:
        float: Коэффициент уравнения
    """
    # Пытаемся один раз прочитать из argv
    coef_str = None
    if len(sys.argv) > index:
        coef_str = sys.argv[index]

    # Цикл: пробуем преобразовать в float, пока не получится
    while True:
        if coef_str is None:
            print(prompt)
            coef_str = input()
        try:
            return float(coef_str)
        except ValueError:
            print(f"Некорректное значение: '{coef_str}'. Введите число заново.")
            coef_str = None  # дальше только input()


def solve_biquadratic(a, b, c):
    """
    Решение биквадратного уравнения a*x^4 + b*x^2 + c = 0.

    Returns:
        list[float]: список действительных корней (может быть пустым)
    """
    roots = []

    # Если a == 0 — это уже не биквадратное, но обработаем аккуратно
    if a == 0:
        # b*x^2 + c = 0  ->  x^2 = -c/b
        if b == 0:
            return roots  # c = 0 даёт бесконечно много решений, не наш случай
        y = -c / b
        if y > 0:
            sq = math.sqrt(y)
            roots.extend([sq, -sq])
        elif y == 0:
            roots.append(0.0)
        return roots

    # Основной случай: ay^2 + by + c = 0, y = x^2
    D = b * b - 4 * a * c

    if D < 0:
        return roots  # нет действительных y, значит нет и x

    if D == 0:
        y = -b / (2 * a)
        if y > 0:
            sq = math.sqrt(y)
            roots.extend([sq, -sq])
        elif y == 0:
            roots.append(0.0)
        return roots

    # D > 0 — два y
    sqD = math.sqrt(D)
    y1 = (-b + sqD) / (2 * a)
    y2 = (-b - sqD) / (2 * a)

    for y in (y1, y2):
        if y > 0:
            sq = math.sqrt(y)
            roots.extend([sq, -sq])
        elif y == 0:
            roots.append(0.0)

    return roots


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
