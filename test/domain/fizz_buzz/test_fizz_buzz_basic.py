import unittest

from domain.fizz_buzz.basic import map_from_integer_to_fizz_or_buzz, \
    map_fizz_buzz_number_for_a_range


class TestFizzBuzzBasic(unittest.TestCase):

    def test_an_integer_not_multiple_of_three_or_five_is_printed_it(self):
        self.assertEqual("4", map_from_integer_to_fizz_or_buzz(4))

    def test_an_integer_multiple_of_three_print_fizz(self):
        self.assertEqual("fizz", map_from_integer_to_fizz_or_buzz(9))

    def test_an_integer_multiple_of_five_print_buzz(self):
        self.assertEqual("buzz", map_from_integer_to_fizz_or_buzz(10))

    def test_a_list_add_fizz_an_integer_and_buzz(self):
        self.assertEqual(["fizz", "4", "buzz"], map_fizz_buzz_number_for_a_range(start=3, end=5))

    def test_a_list_add_accumulated_fizz_an_integer_and_buz(self):
        self.assertEqual(["fizzbuzz", "16", "17"], map_fizz_buzz_number_for_a_range(start=15, end=17))


if __name__ == '__main__':
    unittest.main()
