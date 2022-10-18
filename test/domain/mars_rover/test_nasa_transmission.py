import unittest

from domain.mars_rover.nasa_transmission import translator


class TestNasaTransmission(unittest.TestCase):
    def test_convert_string_order_to_final_position(self):
        self.assertEqual("1 3 N", translator("5 5\n1 2 N\nLMLMLMLMM)"))
                                                                      # add assertion here
    def test_convert_string_orders_to_final_position(self):
        self.assertEqual("1 3 N\n5 1 E", translator("5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM"))  # add assertion here

    def test_convert_more_than_two_rovers_order_to_final_position(self):
        self.assertEqual("1 3 N\n5 1 E\n2 2 N", translator("5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM\n0 0 N\nMMRMML"))


if __name__ == '__main__':
    unittest.main()
