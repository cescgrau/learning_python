from domain.mars_rover.direction import Direction
from domain.mars_rover.grid_limits import GridLimits
from domain.mars_rover.mars_rover import Rover


def translator(an_input: str) -> str:
    result = ""
    items = an_input.split("\n")
    rover_total = int((len(items) - 1) / 2)
    limits = GridLimits(x=int(items[0][0]), y=int(items[0][2]))
    for rover_count in range(0, rover_total):
        rover_position_definition = rover_count * 2 + 1
        rover_movement_definition = rover_count * 2 + 2
        n_rover = Rover(x_position=int(items[rover_position_definition][0]),
                        y_position=int(items[rover_position_definition][2]),
                        direction_view=Direction(items[rover_position_definition][4]),
                        limits=limits)
        movements = items[rover_movement_definition]
        result += calculate_final_position(n_rover, movements)
    return result.strip()


def calculate_final_position(rover, movements):
    result = ""
    for movement in movements:
        if movement == "L":
            rover.turn_left()
        elif movement == "R":
            rover.turn_right()
        elif movement == "M":
            rover.move()
    result += f"{rover.x_position} {rover.y_position} {rover.direction_view.value}\n"
    return result
