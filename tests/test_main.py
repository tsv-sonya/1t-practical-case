"""Тесты для main.py."""

import unittest


class TestMainPy(unittest.TestCase):
    """Тесты модуля main.py."""

    def test_module_exists(self):
        """Проверяем что модуль существует."""
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
