import unittest

from domain.fizz_buzz.extended import map_from_integer_to_fizz_and_buzz_extended, \
    map_fizz_buzz_multiple_and_with_threes_and_fives_for_a_range


class TestFizzBuzzExtended(unittest.TestCase):

    def test_a_list_add_fizz_an_integer_and_buzz_extended(self):
        self.assertEqual(["fizzfizz", "4", "buzzbuzz"],
                         map_fizz_buzz_multiple_and_with_threes_and_fives_for_a_range(start=3, end=5))

    def test_an_integer_has_three_inside_print_fizz(self):
        self.assertEqual("fizz", map_from_integer_to_fizz_and_buzz_extended(13))

    def test_an_integer_has_five_inside_print_buzz(self):
        self.assertEqual("buzz", map_from_integer_to_fizz_and_buzz_extended(52))

    def test_an_integer_has_three_and_five_inside_and_is_multiple_of_five_print_fizzbuzzbuzz(self):
        self.assertEqual("fizzbuzzbuzz", map_from_integer_to_fizz_and_buzz_extended(35))

    def test_an_integer_has_five_and_three_inside_print_buzzfizz(self):
        self.assertEqual("fizzbuzz", map_from_integer_to_fizz_and_buzz_extended(53))

    def test_an_integer_has_three_and_five_inside_and_is_multiple_of_five_and_is_multiple_of_three_print_fizzbuzzbuzzfizz(
            self):
        self.assertEqual("fizzbuzzbuzzfizz", map_from_integer_to_fizz_and_buzz_extended(315))


if __name__ == '__main__':
    unittest.main()
