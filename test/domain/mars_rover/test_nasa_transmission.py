import unittest

from domain.mars_rover.direction import Direction
from domain.mars_rover.grid_limits import GridLimits
from domain.mars_rover.mars_rover import Rover


def translator(input: str) -> str:
    items = input.split("\n")
    limits = GridLimits(x=int(items[0][0]), y=int(items[0][2]))
    first_rover = Rover(x_position=int(items[1][0]), y_position=int(items[1][2]), direction_view=Direction(items[1][4]),
                        limits=limits)
    movements = items[2]
    for movement in movements:
        if movement == "L":
            first_rover.turn_left()
        elif movement == "R":
            first_rover.turn_right()
        elif movement == "M":
            first_rover.move()

    second_rover = Rover(x_position=int(items[3][0]), y_position=int(items[3][2]),
                         direction_view=Direction(items[3][4]),
                         limits=limits)

    movements = items[4]
    for movement in movements:
        if movement == "L":
            second_rover.turn_left()
        elif movement == "R":
            second_rover.turn_right()
        elif movement == "M":
            second_rover.move()

    result = f"{first_rover.x_position} {first_rover.y_position} {first_rover.direction_view.value}\n"
    result += f"{second_rover.x_position} {second_rover.y_position} {second_rover.direction_view.value}"

    return result


class TestNasaTransmission(unittest.TestCase):
    def test_convert_string_orders_to_final_position(self):
        self.assertEqual("1 3 N\n5 1 E", translator("5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
