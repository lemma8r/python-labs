"""Шаги для BDD-сценариев (behave)."""

import os
import sys

from behave import given, when, then

# Чтобы import biquadratic работал из features/steps/
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

from biquadratic import solve_biquadratic  # noqa: E402


@given("коэффициенты уравнения a={a:g}, b={b:g}, c={c:g}")
def step_given_coefficients(context, a, b, c):
    context.a = a
    context.b = b
    context.c = c


@when("я решаю биквадратное уравнение")
def step_when_solve(context):
    context.roots = solve_biquadratic(context.a, context.b, context.c)


@then("я получаю {n:d} корня")
@then("я получаю {n:d} корней")
@then("я получаю {n:d} корень")
def step_then_count(context, n):
    assert len(context.roots) == n, (
        f"Ожидалось {n} корней, получено {len(context.roots)}: {context.roots}"
    )


@then("корни равны {expected}")
def step_then_values(context, expected):
    exp = sorted(float(x) for x in expected.split(","))
    got = sorted(context.roots)
    assert len(exp) == len(got), f"Разное число корней: {exp} vs {got}"
    for e, g in zip(exp, got):
        assert abs(e - g) < 1e-9, f"Корень {g} != {e}"
