import unittest

from domain.string_calculator.add import add_internal, add
from domain.string_calculator.tools import has_separator_specification, extract_separator


class TestStringCalculator(unittest.TestCase):
    def test_an_empty_string_adds_zero(self):
        self.assertEqual(0, add_internal(""))  # add assertion here

    def test_a_string_with_one_number_adds_this_number(self):
        self.assertEqual(5, add_internal("5"))

    def test_a_string_with_two_numbers_add_these_numbers(self):
        self.assertEqual(3, add_internal("1,2"))

    def test_a_string_with_five_numbers_add_these_numbers(self):
        self.assertEqual(15, add_internal("1,2,3,4,5"))

    def test_a_string_with_two_separators_together_fails(self):
        with self.assertRaises(ValueError):
            add_internal("8,,8")

    def test_split_string_with_new_line_separator(self):
        self.assertEqual(3, add_internal("1\n2"))

    def test_string_contains_two_sequential_separators_fails(self):
        with self.assertRaises(ValueError):
            add_internal("8,\n8")

    def test_a_string_with_numbers_add_these_numbers_with_a_separator_specified(self):
        self.assertEqual(15, add_internal("1;2;3;4;5", separators=[";"]))

    def popo(self):
        self.assertEqual(3, add("//;\n1;2"))

    def test_the_string_contains_two_first_characters_to_spec_a_delimiter(self):
        self.assertTrue(
            has_separator_specification(a_string_with_numbers="//;\n8;8;8"))

    def test_the_string_not_contains_two_first_characters_to_spec_a_delimiter(self):
        self.assertFalse(has_separator_specification(a_string_with_numbers="12;3"))

    def test_in_case_of_a_new_delimiter_obtain_this_character(self):
        self.assertEqual(";", extract_separator(a_string_with_numbers="//;\n3;4"))
        self.assertEqual(",", extract_separator(a_string_with_numbers="//,\n3,4"))


if __name__ == '__main__':
    unittest.main()
