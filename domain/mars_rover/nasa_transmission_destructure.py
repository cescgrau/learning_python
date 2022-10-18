from domain.mars_rover.direction import Direction
from domain.mars_rover.grid_limits import GridLimits
from domain.mars_rover.mars_rover import Rover


def translator_destructuring(an_input: str) -> str:
    result = []
    items = an_input.split("\n")
    [limits_definition, *rest] = items
    limits = build_limits(limits_definition)
    while rest:
        [rover_definition, rover_movements, *rest] = rest
        rover = build_rover(rover_definition, limits)
        result += [calculate_rover_final_position(rover, rover_movements)]
    return "\n".join(result)


def build_limits(limits_definition: str) -> GridLimits:
    [max_x, max_y] = limits_definition.split(" ")
    limits = GridLimits(x=int(max_x), y=int(max_y))
    return limits


def build_rover(rover: str, limits: GridLimits) -> Rover:
    [initial_x, initial_y, direction] = rover.split(" ")
    rover = Rover(x_position=int(initial_x),
                  y_position=int(initial_y),
                  direction_view=Direction(direction),
                  limits=limits)
    return rover


def calculate_rover_final_position(rover: Rover, movements: str) -> str:
    for movement in movements:
        if movement == "L":
            rover.turn_left()
        elif movement == "R":
            rover.turn_right()
        elif movement == "M":
            rover.move()
    return f"{rover.x_position} {rover.y_position} {rover.direction_view.value}"
