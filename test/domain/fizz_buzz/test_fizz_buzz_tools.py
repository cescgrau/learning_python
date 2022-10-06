import unittest

from domain.fizz_buzz.tools import is_number_three_into_the_number, \
    is_number_five_into_the_number, is_multiple_of, is_number_a_into


class TestFizzBuzzTools(unittest.TestCase):

    def test_an_integer_is_multiple_of(self):
        self.assertTrue(is_multiple_of(multiple=3, a_number=9))
        self.assertTrue(is_multiple_of(multiple=5, a_number=15))
        self.assertFalse(is_multiple_of(multiple=3, a_number=10))
        self.assertFalse(is_multiple_of(multiple=5, a_number=18))
        self.assertTrue(is_multiple_of(multiple=3 and 5, a_number=15))
        self.assertFalse(is_multiple_of(multiple=3 and 5, a_number=16))

    def test_should_return_true_if_an_integer_contains_three(self):
        self.assertTrue(is_number_three_into_the_number(3))

    def test_should_return_false_if_an_integer_not_contains_three(self):
        self.assertFalse(is_number_three_into_the_number(4))

    def test_should_return_true_if_an_integer_contains_five(self):
        self.assertTrue(is_number_five_into_the_number(5))

    def test_should_return_true_if_an_integer_not_contains_five(self):
        self.assertFalse(is_number_five_into_the_number(44))

    def test_contains_a(self):
        self.assertTrue(is_number_a_into(character="3", a_number=35))
        self.assertTrue(is_number_a_into(character="5", a_number=35))
        self.assertFalse(is_number_a_into(character="3", a_number=45))
        self.assertFalse(is_number_a_into(character="5", a_number=33))




if __name__ == '__main__':
    unittest.main()
