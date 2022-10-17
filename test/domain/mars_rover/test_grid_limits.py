import unittest

from domain.mars_rover.grid_limits import GridLimits


class TestGridLimits(unittest.TestCase):
    def test_initial_plateau_parameters(self):

        limits = GridLimits(5, 6)
        self.assertEqual(5, limits.x)
        self.assertEqual(6, limits.y)  # add assertion here


if __name__ == '__main__':
    unittest.main()
