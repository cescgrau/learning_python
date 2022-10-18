from domain.mars_rover.direction import Direction
from domain.mars_rover.grid_limits import GridLimits
from domain.mars_rover.mars_rover import Rover


def translator(an_input: str) -> str:
    items = an_input.split("\n")
    rover_total = int((len(items)-1)/2)
    limits = GridLimits(x=int(items[0][0]), y=int(items[0][2]))
    result = ""
    for rover_count in range(0, rover_total):
        n_rover = Rover(x_position=int(items[rover_count*2+1][0]),
                        y_position=int(items[rover_count*2+1][2]),
                        direction_view=Direction(items[rover_count*2+1][4]),
                        limits=limits)
        movements = items[rover_count*2 + 2]
        for movement in movements:
            if movement == "L":
                n_rover.turn_left()
            elif movement == "R":
                n_rover.turn_right()
            elif movement == "M":
                n_rover.move()
        result += f"{n_rover.x_position} {n_rover.y_position} {n_rover.direction_view.value}\n"
    return result.strip()
