import unittest

from domain.mars_rover.direction import Direction
from domain.mars_rover.mars_rover import Rover


class TheRoverTest(unittest.TestCase):

    def test_initialization_parameters_are_honoured(self):
        rover_inside_plateau = Rover(2, 3, Direction.N)
        self.assertEqual(2, rover_inside_plateau.x_position)
        self.assertEqual(3, rover_inside_plateau.y_position)
        self.assertEqual(Direction.N, rover_inside_plateau.direction_view)

    def test_the_movement_increases_y_when_direction_is_north(self):
        rover_inside_plateau = Rover(2, 3, Direction.N)
        rover_inside_plateau.move()
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_movement_increases_x_when_direction_is_east(self):
        rover_inside_plateau = Rover(2, 4, Direction.E)
        rover_inside_plateau.move()
        self.assertEqual(3, rover_inside_plateau.x_position)
        self.assertEqual(4, rover_inside_plateau.y_position)

    def test_the_movement_decreases_x_when_direction_is_west(self):
        rover_inside_plateau = Rover(2, 4, Direction.W)
        rover_inside_plateau.move()
        self.assertEqual(1, rover_inside_plateau.x_position)
        self.assertEqual(4, rover_inside_plateau.y_position)

    def test_the_movement_decreases_y_when_direction_is_south(self):
        rover_inside_plateau = Rover(2, 4, Direction.S)
        rover_inside_plateau.move()
        self.assertEqual(2, rover_inside_plateau.x_position)
        self.assertEqual(3, rover_inside_plateau.y_position)

    def test_the_turn_right_from_north_turn_to_east(self):
        rover_inside_plateau = Rover(2, 4, Direction.N)
        rover_inside_plateau.turn_right()
        self.assertEqual(Direction.E, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_turn_right_from_east_turn_to_south(self):
        rover_inside_plateau = Rover(2, 4, Direction.E)
        rover_inside_plateau.turn_right()
        self.assertEqual(Direction.S, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_turn_right_from_south_turn_to_west(self):
        rover_inside_plateau = Rover(2, 4, Direction.S)
        rover_inside_plateau.turn_right()
        self.assertEqual(Direction.W, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_turn_right_from_west_turn_to_north(self):
        rover_inside_plateau = Rover(2, 4, Direction.W)
        rover_inside_plateau.turn_right()
        self.assertEqual(Direction.N, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_turn_left_from_north_turn_to_west(self):
        rover_inside_plateau = Rover(2, 4, Direction.N)
        rover_inside_plateau.turn_left()
        self.assertEqual(Direction.W, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_turn_left_from_west_turn_to_south(self):
        rover_inside_plateau = Rover(2, 4, Direction.W)
        rover_inside_plateau.turn_left()
        self.assertEqual(Direction.S, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_turn_left_from_south_turn_to_east(self):
        rover_inside_plateau = Rover(2, 4, Direction.S)
        rover_inside_plateau.turn_left()
        self.assertEqual(Direction.E, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_turn_left_from_east_turn_to_north(self):
        rover_inside_plateau = Rover(2, 4, Direction.E)
        rover_inside_plateau.turn_left()
        self.assertEqual(Direction.N, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

if __name__ == '__main__':
    unittest.main()
