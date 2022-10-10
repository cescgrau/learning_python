import unittest

from domain.fizz_buzz.tools import is_multiple_of, is_character_into


class TestFizzBuzzTools(unittest.TestCase):

    def test_is_multiple_of_return_true_if_it_is_multiple(self):
        self.assertTrue(is_multiple_of(multiple=3, a_number=9))
        self.assertTrue(is_multiple_of(multiple=5, a_number=15))
        self.assertFalse(is_multiple_of(multiple=3, a_number=10))
        self.assertFalse(is_multiple_of(multiple=5, a_number=18))
        self.assertTrue(is_multiple_of(multiple=3 and 5, a_number=15))
        self.assertFalse(is_multiple_of(multiple=3 and 5, a_number=16))

    def test_contains_a_returns_true_if_character_is_contained_in_a_number(self):
        self.assertTrue(is_character_into(character="3", a_number=35))
        self.assertTrue(is_character_into(character="5", a_number=35))
        self.assertFalse(is_character_into(character="3", a_number=45))
        self.assertFalse(is_character_into(character="5", a_number=33))


if __name__ == '__main__':
    unittest.main()
