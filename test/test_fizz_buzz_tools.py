import unittest

from domain.fizz_buzz.basic import is_multiple_of_five, is_multiple_of_three
from domain.fizz_buzz.extended import is_number_five_into_the_number, is_number_three_into_the_number


class TestFizzBuzzTools(unittest.TestCase):
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

    def test_should_return_true_if_an_integer_contains_three(self):
        self.assertTrue(is_number_three_into_the_number(3))

    def test_should_return_false_if_an_integer_not_contains_three(self):
        self.assertFalse(is_number_three_into_the_number(4))

    def test_should_return_true_if_an_integer_contains_five(self):
        self.assertTrue(is_number_five_into_the_number(5))

    def test_should_return_true_if_an_integer_not_contains_five(self):
        self.assertFalse(is_number_five_into_the_number(44))


if __name__ == '__main__':
    unittest.main()
