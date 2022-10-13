import unittest

from domain.fizz_buzz_revisited.fizz_buzz_revisited import is_multiple_of, replacing_multiple_of, replacing_integers
from domain.fizz_buzz_revisited.fizz_buzz_tools_revisited import a_returning_a_list_of_integers


class TestFizzBuzz(unittest.TestCase):
    def test_contains_a_three_and_replace_for_a_Fizz(self):
        self.assertEqual([1,2,"fizz"], replacing_integers(1,4))

    def test_contains_a_five_and_replace_for_a_buzz(self):
        self.assertEqual([4,"buzz"], replacing_integers(4,6))

    def test_contains_an_integer(self):
        self.assertEqual([1, 2, "fizz", 4, "buzz"], replacing_integers(1, 6))

    def test_if_a_integer_is_multiple_of_a_divider(self):
        self.assertTrue(is_multiple_of(18, 3))
        self.assertTrue(is_multiple_of(15, 5))
        self.assertFalse(is_multiple_of(9, 5))
        self.assertFalse(is_multiple_of(20, 3))
        # add assertion here

    def test_returning_a_list_of_integers(self):
        self.assertEqual([1, 2, 3, 4, 5], a_returning_a_list_of_integers(start=1, end=6))

    def test_replacing_multiple_of_three_for_fizz(self):
        self.assertEqual([1, 2, "fizz"], replacing_multiple_of(1, 4))

    def test_replacing_multiple_of_five_for_buzz(self):
        self.assertEqual([4, "buzz"], replacing_multiple_of(4, 6))

    def test_replacing_multiple_of_three_for_bizz_and_five_for_buzz(self):
        self.assertEqual([1, 2, "fizz", 4, "buzz"], replacing_multiple_of(start=1, end=6))

    def test_replacing_multiples_of_three_and_five_adding_words_fizz_buzz(self):
        self.assertEqual(["buzz", 11, "fizz", 13, 14, "fizzbuzz"], replacing_multiple_of(10, 16))


if __name__ == '__main__':
    unittest.main()
