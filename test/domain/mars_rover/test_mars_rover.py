import unittest

from domain.mars_rover.direction import Direction
from domain.mars_rover.grid_limits import GridLimits
from domain.mars_rover.mars_rover import Rover


class TheRoverTest(unittest.TestCase):

    def test_initialization_parameters_are_honoured(self):
        rover_inside_plateau = Rover(2, 3, Direction.N, GridLimits(5,5))
        self.assertEqual(2, rover_inside_plateau.x_position)
        self.assertEqual(3, rover_inside_plateau.y_position)
        self.assertEqual(Direction.N, rover_inside_plateau.direction_view)

    def test_the_movement_increases_y_when_direction_is_north(self):
        rover_inside_plateau = Rover(2, 3, Direction.N, GridLimits(5,5))
        rover_inside_plateau.move()
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_movement_increases_x_when_direction_is_east(self):
        rover_inside_plateau = Rover(2, 4, Direction.E, GridLimits(5,5))
        rover_inside_plateau.move()
        self.assertEqual(3, rover_inside_plateau.x_position)
        self.assertEqual(4, rover_inside_plateau.y_position)

    def test_the_movement_decreases_x_when_direction_is_west(self):
        rover_inside_plateau = Rover(2, 4, Direction.W, GridLimits(5,5))
        rover_inside_plateau.move()
        self.assertEqual(1, rover_inside_plateau.x_position)
        self.assertEqual(4, rover_inside_plateau.y_position)

    def test_the_movement_decreases_y_when_direction_is_south(self):
        rover_inside_plateau = Rover(2, 4, Direction.S, GridLimits(5,5))
        rover_inside_plateau.move()
        self.assertEqual(2, rover_inside_plateau.x_position)
        self.assertEqual(3, rover_inside_plateau.y_position)

    def test_the_turn_right_from_north_turn_to_east(self):
        rover_inside_plateau = Rover(2, 4, Direction.N, GridLimits(5,5))
        rover_inside_plateau.turn_right()
        self.assertEqual(Direction.E, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_turn_right_from_east_turn_to_south(self):
        rover_inside_plateau = Rover(2, 4, Direction.E, GridLimits(5,5))
        rover_inside_plateau.turn_right()
        self.assertEqual(Direction.S, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_turn_right_from_south_turn_to_west(self):
        rover_inside_plateau = Rover(2, 4, Direction.S, GridLimits(5,5))
        rover_inside_plateau.turn_right()
        self.assertEqual(Direction.W, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_turn_right_from_west_turn_to_north(self):
        rover_inside_plateau = Rover(2, 4, Direction.W, GridLimits(5,5))
        rover_inside_plateau.turn_right()
        self.assertEqual(Direction.N, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_turn_left_from_north_turn_to_west(self):
        rover_inside_plateau = Rover(2, 4, Direction.N, GridLimits(5,5))
        rover_inside_plateau.turn_left()
        self.assertEqual(Direction.W, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_turn_left_from_west_turn_to_south(self):
        rover_inside_plateau = Rover(2, 4, Direction.W, GridLimits(5,5))
        rover_inside_plateau.turn_left()
        self.assertEqual(Direction.S, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_turn_left_from_south_turn_to_east(self):
        rover_inside_plateau = Rover(2, 4, Direction.S, GridLimits(5,5))
        rover_inside_plateau.turn_left()
        self.assertEqual(Direction.E, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_the_turn_left_from_east_turn_to_north(self):
        rover_inside_plateau = Rover(2, 4, Direction.E, GridLimits(5,5))
        rover_inside_plateau.turn_left()
        self.assertEqual(Direction.N, rover_inside_plateau.direction_view)
        self.assertEqual(4, rover_inside_plateau.y_position)
        self.assertEqual(2, rover_inside_plateau.x_position)

    def test_assuming_a_initial_position_and_a_list_of_movements_obtain_a_final_position_13n(self):
        rover_inside_plateau = Rover(1, 2, Direction.N, GridLimits(5,5))
        rover_inside_plateau.turn_left()
        rover_inside_plateau.move()
        rover_inside_plateau.turn_left()
        rover_inside_plateau.move()
        rover_inside_plateau.turn_left()
        rover_inside_plateau.move()
        rover_inside_plateau.turn_left()
        rover_inside_plateau.move()
        rover_inside_plateau.move()
        self.assertEqual(1, rover_inside_plateau.x_position)
        self.assertEqual(3, rover_inside_plateau.y_position)
        self.assertEqual(Direction.N, rover_inside_plateau.direction_view)

    def test_assuming_a_initial_position_and_a_list_of_movements_obtain_a_final_position_51e(self):
        rover_inside_plateau = Rover(3, 3, Direction.E, GridLimits(5,5))
        rover_inside_plateau.move()
        rover_inside_plateau.move()
        rover_inside_plateau.turn_right()
        rover_inside_plateau.move()
        rover_inside_plateau.move()
        rover_inside_plateau.turn_right()
        rover_inside_plateau.move()
        rover_inside_plateau.turn_right()
        rover_inside_plateau.turn_right()
        rover_inside_plateau.move()
        self.assertEqual(5, rover_inside_plateau.x_position)
        self.assertEqual(1, rover_inside_plateau.y_position)
        self.assertEqual(Direction.E, rover_inside_plateau.direction_view)

    def test_the_rover_movement_is_not_allowed_for_being_out_of_limits_of_north(self):
        rover_inside_plateau = Rover(5,5,Direction.N, GridLimits(5,5))
        rover_inside_plateau.move()
        self.assertEqual(5, rover_inside_plateau.y_position)
    def test_the_rover_movement_is_not_allowed_for_being_out_of_limits_of_east(self):
        rover_inside_plateau = Rover(5,5,Direction.E, GridLimits(5,5))
        rover_inside_plateau.move()
        self.assertEqual(5, rover_inside_plateau.x_position)
    def test_the_rover_movement_is_not_allowed_for_being_out_of_limits_of_south(self):
        rover_inside_plateau = Rover(0,0,Direction.S, GridLimits(5,5))
        rover_inside_plateau.move()
        self.assertEqual(0, rover_inside_plateau.y_position)

    def test_the_rover_movement_is_not_allowed_for_being_out_of_limits_of_west(self):
        rover_inside_plateau = Rover(0,0,Direction.W, GridLimits(5,5))
        rover_inside_plateau.move()
        self.assertEqual(0, rover_inside_plateau.x_position)

    def test_assuming_a_initial_position_and_a_list_of_movements_far_away_from_limits_obtain_a_final_position(self):
        rover_inside_plateau = Rover(3, 3, Direction.E, GridLimits(5,5))
        rover_inside_plateau.move()
        rover_inside_plateau.move()
        rover_inside_plateau.move()
        rover_inside_plateau.move()
        self.assertEqual(5, rover_inside_plateau.x_position)
        self.assertEqual(3, rover_inside_plateau.y_position)
        self.assertEqual(Direction.E, rover_inside_plateau.direction_view)



if __name__ == '__main__':
    unittest.main()

