import unittest

from domain.math.lists import add_two_lists_of_three_elements


class TestAddListValues(unittest.TestCase):
    def test_should_add_lists_with_the_same_length(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        lists_added = add_two_lists_of_three_elements(list1, list2)
        self.assertEqual([5, 7, 9], lists_added)  # add assertion here

    def test_should_rise_an_exception_if_lists_do_not_have_the_same_length(self):
        with self.assertRaises(ValueError):
            list1 = [1, 2, 3, 4]
            list2 = [4, 5, 6]
            add_two_lists_of_three_elements(list1, list2)

    def test_lists_should_added_for_any_length_of_the_lists(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, 2, 3, 4, 5]
        elements = add_two_lists_of_three_elements(list1, list2)
        self.assertEqual([2, 4, 6, 8, 10], elements)

        if __name__ == '__main__':
            unittest.main()
