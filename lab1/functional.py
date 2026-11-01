"""
Лабораторная работа №1. Биквадратное уравнение.
Функциональная парадигма: сопоставление с образцом (match/case).

Уравнение: a*x^4 + b*x^2 + c = 0
Замена:    y = x^2, y >= 0
"""

import sys
import math
from typing import Optional


#  Чистые функции для чтения коэффициентов

def parse_float(s: str) -> Optional[float]:
    """Пытается преобразовать строку в float. Возвращает None при ошибке."""
    try:
        return float(s)
    except ValueError:
        return None


def read_coef(argv: list, index: int, prompt: str) -> float:
    """
    Функциональный подход: читаем коэффициент через рекурсию.
    Если из argv не удалось — переходим на ввод с клавиатуры.
    """
    from_argv = argv[index] if len(argv) > index else None

    def try_parse(raw: Optional[str]) -> float:
        match raw:
            # случай 1: из argv пришла строка, парсится
            case str() if parse_float(raw) is not None:
                return parse_float(raw)
            # случай 2: из argv пришла строка, не парсится → ругаемся и вводим заново
            case str():
                print(f"Некорректное значение: '{raw}'. Введите число заново.")
                return try_parse(None)
            # случай 3: None → ввод с клавиатуры
            case None:
                print(prompt)
                return try_parse(input())
            # запасной вариант (не должен случиться)
            case _:
                return try_parse(None)

    return try_parse(from_argv)


#  Чистые функции для решения

def roots_from_y(y: float) -> list:
    """
    Из значения y = x^2 получаем корни x.
    Сопоставление с образцом по знаку y.
    """
    match y:
        case y if y > 0:
            sq = math.sqrt(y)
            return [sq, -sq]
        case 0:
            return [0.0]
        case _:
            return []


def solve_biquadratic(a: float, b: float, c: float) -> list:
    """
    Решение биквадратного уравнения a*x^4 + b*x^2 + c = 0.
    Возвращает список действительных корней.
    """
    match (a, b, c):
        # вырожденные случаи: a == 0
        case (0, 0, _):
            return []
        case (0, b_val, c_val):
            y = -c_val / b_val
            return roots_from_y(y)

        # основной случай: считаем дискриминант
        case (a_val, b_val, c_val):
            D = b_val * b_val - 4 * a_val * c_val
            match D:
                case d if d < 0:
                    return []
                case 0:
                    y = -b_val / (2 * a_val)
                    return roots_from_y(y)
                case d if d > 0:
                    sqD = math.sqrt(d)
                    y1 = (-b_val + sqD) / (2 * a_val)
                    y2 = (-b_val - sqD) / (2 * a_val)
                    return roots_from_y(y1) + roots_from_y(y2)


def format_roots(roots: list) -> str:
    """Формирует строку для вывода. Тоже через match/case."""
    match roots:
        case []:
            return "Нет действительных корней"
        case [r]:
            return f"Один корень: {r}"
        case [r1, r2]:
            return f"Два корня: {r1} и {r2}"
        case [r1, r2, r3]:
            return f"Три корня: {r1}, {r2} и {r3}"
        case [r1, r2, r3, r4]:
            return f"Четыре корня: {r1}, {r2}, {r3} и {r4}"
        case _:
            return f"Корни: {roots}"


#  Точка входа

def main():
    a = read_coef(sys.argv, 1, "Введите коэффициент А:")
    b = read_coef(sys.argv, 2, "Введите коэффициент B:")
    c = read_coef(sys.argv, 3, "Введите коэффициент C:")

    print(f"Уравнение: {a}*x^4 + {b}*x^2 + {c} = 0")
    roots = solve_biquadratic(a, b, c)
    print(format_roots(roots))


if __name__ == "__main__":
    main()
