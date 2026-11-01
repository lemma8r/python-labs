"""
TDD-тесты (unittest) для биквадратного уравнения.
Не менее 3 тестов — здесь 6.
"""

import unittest

from biquadratic import solve_biquadratic, roots_from_y


class TestSolveBiquadratic(unittest.TestCase):

    def test_four_roots(self):
        """x^4 - 5x^2 + 4 = 0 -> корни -2, -1, 1, 2."""
        roots = solve_biquadratic(1, -5, 4)
        self.assertEqual(len(roots), 4)
        expected = sorted([-2.0, -1.0, 1.0, 2.0])
        self.assertEqual(sorted(roots), expected)

    def test_two_roots(self):
        """x^4 - 1 = 0 -> корни -1, 1."""
        roots = solve_biquadratic(1, 0, -1)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(sorted(roots)[0], -1.0)
        self.assertAlmostEqual(sorted(roots)[1], 1.0)

    def test_no_roots(self):
        """x^4 + 1 = 0 -> действительных корней нет."""
        roots = solve_biquadratic(1, 0, 1)
        self.assertEqual(roots, [])

    def test_zero_root(self):
        """x^4 = 0 -> единственный корень 0."""
        roots = solve_biquadratic(1, 0, 0)
        self.assertEqual(roots, [0.0])

    def test_degenerate_a_zero(self):
        """a = 0: x^2 - 4 = 0 -> корни -2, 2."""
        roots = solve_biquadratic(0, 1, -4)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(sorted(roots)[0], -2.0)
        self.assertAlmostEqual(sorted(roots)[1], 2.0)

    def test_roots_from_y_negative(self):
        """y < 0 -> корней нет."""
        self.assertEqual(roots_from_y(-1), [])


if __name__ == "__main__":
    unittest.main()
