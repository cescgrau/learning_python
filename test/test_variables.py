import unittest


class TestVariables(unittest.TestCase):
    def test_a_variable_can_hold_an_integer(self):
        an_integer = 3
        self.assertEqual(3, an_integer)  # add assertion here

    def test_a_variable_can_hold_a_string(self):
        a_string = "world"
        self.assertEqual("world", a_string)

    def test_a_variable_can_hold_a_float(self):
        a_float = 1.2
        self.assertEqual(1.2, a_float)

    def test_a_variable_can_hold_a_list(self):
        a_list = [1, 2, 3]
        self.assertEqual([1, 2, 3], a_list)


if __name__ == "__main__":
    unittest.main()
