import unittest

from domain.fizz_buzz.fizz_buzz import is_multiple_of_five, is_multiple_of_three, map_from_integer_to_fizz_or_buzz, \
    map_fizz_buzz_number_for_a_range


def is_number_three_into_the_number(a_number):
    return "3" in str(a_number)


def is_number_five_into_the_number(a_number):
    return "5" in str(a_number)


def map_from_integer_contains_three_or_five_to_fizz_or_buzz(a_number):
    if is_number_three_into_the_number(a_number):
        return "fizz"
    if is_number_five_into_the_number(a_number):
        return "buzz"
    return str(a_number)


class TestFizzBuzzExtended(unittest.TestCase):

    def test_an_integer_multiple_of_five_is_identified(self):
        an_integer_result = is_multiple_of_five(10)
        self.assertTrue(an_integer_result)

    def test_an_integer_not_multiple_of_five_is_identified(self):
        an_integer_result = is_multiple_of_five(8)
        self.assertFalse(an_integer_result)

    def test_an_integer_multiple_of_three_is_identified(self):
        an_integer_result = is_multiple_of_three(9)
        self.assertTrue(an_integer_result)

    def test_an_integer_not_multiple_of_three_is_identified(self):
        an_integer_result = is_multiple_of_three(8)
        self.assertFalse(an_integer_result)

    def test_an_integer_not_multiple_of_three_or_five_is_printed_it(self):
        self.assertEqual("4", map_from_integer_to_fizz_or_buzz(4))

    def test_an_integer_multiple_of_three_print_fizz(self):
        self.assertEqual("fizz", map_from_integer_to_fizz_or_buzz(9))

    def test_an_integer_multiple_of_five_print_buzz(self):
        self.assertEqual("buzz", map_from_integer_to_fizz_or_buzz(10))

    def test_a_list_add_fizz_an_integer_and_buzz(self):
        self.assertEqual(["fizz", "4", "buzz"], map_fizz_buzz_number_for_a_range(start=3, end=5))

    def test_should_return_true_if_an_integer_contains_three(self):
        self.assertTrue(is_number_three_into_the_number(3))

    def test_should_return_false_if_an_integer_not_contains_three(self):
        self.assertFalse(is_number_three_into_the_number(4))

    def test_should_return_true_if_an_integer_contains_five(self):
        self.assertTrue(is_number_five_into_the_number(5))

    def test_should_return_true_if_an_integer_not_contains_five(self):
        self.assertFalse(is_number_five_into_the_number(44))

    def test_an_integer_has_three_inside_print_fizz(self):
        self.assertEqual("fizz", map_from_integer_contains_three_or_five_to_fizz_or_buzz(34))

    def test_an_integer_has_five_inside_print_buzz(self):
        self.assertEqual("buzz", map_from_integer_contains_three_or_five_to_fizz_or_buzz(35))


if __name__ == '__main__':
    unittest.main()
