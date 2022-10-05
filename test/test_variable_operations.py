import unittest

from domain.math.lists import add_two_lists_of_three_elements


class TestVariableOperations(unittest.TestCase):
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    def test_integers_can_be_added(self):
        integer1 = 1
        integer2 = 2
        result_adding_integers = integer1 + integer2
        self.assertEqual(3, result_adding_integers)  # add assertion here

    def test_strings_can_be_added(self):
        string1 = "sunny"
        string2 = "day"
        strings_added = string1 + " " + string2
        self.assertEqual("sunny day", strings_added)

    def test_lists_can_be_added(self):
        lists_added = self.list1 + self.list2
        self.assertEqual([1, 2, 3, 4, 5, 6], lists_added)

    def test_list_values_can_be_integers_and_strings(self):
        list1 = [1, "day", 3]
        self.assertEqual([1, "day", 3], list1)

    def test_list_values_can_be_integers_and_variables(self):
        a_varible_into_a_list = 1.2
        list1 = [1, a_varible_into_a_list, 3]
        self.assertEqual([1, 1.2, 3], list1)

    def test_an_element_within_a_list_can_be_accessed(self):
        self.assertEqual(2, self.list1[1])

    def test_obtain_a_certain_character_inside_a_string(self):
        string1 = "sunny"
        self.assertEqual("u", string1[1])

    def test_lists_values_can_be_added(self):
        list_values_added = add_two_lists_of_three_elements(self.list1, self.list2)
        self.assertEqual([5, 7, 9], list_values_added)


if __name__ == '__main__':
    unittest.main()
