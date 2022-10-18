import unittest
from typing import Callable

from parameterized import parameterized

from domain.mars_rover.nasa_transmission import translator
from domain.mars_rover.nasa_transmission_destructure import translator_destructuring
from domain.mars_rover.nasa_transmission_fsm import translator_fsm


class TestNasaTransmission(unittest.TestCase):
    @parameterized.expand([[translator], [translator_fsm], [translator_destructuring]])
    def test_convert_string_order_to_final_position(self, a_translator: Callable):
        self.assertEqual("1 3 N",
                         a_translator("5 5\n1 2 N\nLMLMLMLMM)"))
        # add assertion here

    @parameterized.expand([[translator], [translator_fsm], [translator_destructuring]])
    def test_convert_string_orders_to_final_position(self, a_translator: Callable):
        self.assertEqual("1 3 N\n5 1 E",
                         a_translator("5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM"))  # add assertion here

    @parameterized.expand([[translator], [translator_fsm],[translator_destructuring]])
    def test_convert_more_than_two_rovers_order_to_final_position(self, a_translator: Callable):
        self.assertEqual("1 3 N\n5 1 E\n2 2 N",
                         a_translator("5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM\n0 0 N\nMMRMML"))


if __name__ == '__main__':
    unittest.main()
