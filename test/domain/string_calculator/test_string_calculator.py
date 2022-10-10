import unittest


def add(a_string_with_numbers: str) -> int:
    result = 0
    last_item_was_a_separator = ""
    for item in a_string_with_numbers:
        separators = [",", "\n", is_sequential_in_the_string_beginning(a_string_with_numbers)]
        is_separator = True if item in separators else False
        if not is_separator:
            result += int(item)
        elif last_item_was_a_separator and is_separator:
            raise ValueError()
        last_item_was_a_separator = is_separator
    return result


def is_sequential_in_the_string_beginning(a_string_with_numbers: str):
    delimiter = ""
    if a_string_with_numbers[1:2] == "//" and a_string_with_numbers[4:5] == "\n":
        delimiter = str(a_string_with_numbers[3])
    return delimiter


class TestStringCalculator(unittest.TestCase):
    def test_an_empty_string_adds_zero(self):
        self.assertEqual(0, add(""))  # add assertion here

    def test_a_string_with_one_number_adds_this_number(self):
        self.assertEqual(5, add("5"))

    def test_a_string_with_two_numbers_add_these_numbers(self):
        self.assertEqual(3, add("1,2"))

    def test_a_string_with_five_numbers_add_these_numbers(self):
        self.assertEqual(15, add("1,2,3,4,5"))

    def test_a_string_with_two_separators_together_fails(self):
        with self.assertRaises(ValueError):
            add("8,,8")

    def test_split_string_with_new_line_separator(self):
        self.assertEqual(3, add("1\n2"))

    def test_string_contains_two_sequential_separators_fails(self):
        with self.assertRaises(ValueError):
            add("8,\n8")

    def test_string_first_positions_contains_sequential_to_define_delimiter(self):
        self.assertTrue(";", is_sequential_in_the_string_beginning("//;\n"))

    def test_string_with_delimiter_specification_add_numbers(self):
        self.assertEqual(5, add("//;\n2;3"))

        if __name__ == '__main__':
            unittest.main()
