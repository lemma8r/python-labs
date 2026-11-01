"""
Mock-тесты (unittest.mock) для get_coef.
Проверяем: чтение из argv и переспрос при некорректном вводе.
"""

import unittest
from unittest.mock import Mock

from biquadratic import get_coef


class TestGetCoefMock(unittest.TestCase):

    def test_reads_from_argv(self):
        """Если в argv есть корректное значение — возвращается оно, input не вызывается."""
        mock_input = Mock()
        value = get_coef(1, "A:", argv=["prog", "2.5"], input_func=mock_input)
        self.assertEqual(value, 2.5)
        mock_input.assert_not_called()

    def test_reprompts_on_invalid_input(self):
        """Некорректный ввод -> переспрос, пока не будет числа."""
        mock_input = Mock(side_effect=["abc", "3.0"])
        value = get_coef(1, "A:", argv=["prog"], input_func=mock_input)
        self.assertEqual(value, 3.0)
        self.assertEqual(mock_input.call_count, 2)

    def test_invalid_argv_falls_back_to_input(self):
        """Некорректный argv -> переход на input."""
        mock_input = Mock(return_value="7")
        value = get_coef(1, "A:", argv=["prog", "oops"], input_func=mock_input)
        self.assertEqual(value, 7.0)
        mock_input.assert_called_once()


if __name__ == "__main__":
    unittest.main()
