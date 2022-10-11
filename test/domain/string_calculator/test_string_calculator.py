import unittest

from domain.string_calculator.add import add


class TestStringCalculator(unittest.TestCase):
    def test_add_a_string_with_separator_specification(self):
        self.assertEqual(3, add("//;\n1;2"))

    def test_add_a_string_without_separator_specification(self):
        self.assertEqual(3, add("1,2"))


if __name__ == '__main__':
    unittest.main()
