from enum import Enum

from domain.mars_rover.direction import Direction
from domain.mars_rover.grid_limits import GridLimits
from domain.mars_rover.mars_rover import Rover


class TranslatorStages(Enum):
    WAITING_FOR_LIMITS = 1
    WAITING_FOR_ROVER_INITIAL_POSITION = 2
    WAITING_FOR_ROVER_MOVEMENTS = 3


def translator_fsm(an_input: str) -> str:
    stage: TranslatorStages = TranslatorStages.WAITING_FOR_LIMITS
    items = an_input.split("\n")
    limits = None
    current_rover = None
    result = ""
    for item in items:
        if stage == TranslatorStages.WAITING_FOR_LIMITS:
            [x, y] = item.split(" ")
            limits = GridLimits(x=int(x), y=int(y))
            stage = TranslatorStages.WAITING_FOR_ROVER_INITIAL_POSITION
        elif stage == TranslatorStages.WAITING_FOR_ROVER_INITIAL_POSITION:
            [x, y, direction] = item.split(" ")
            current_rover = Rover(x_position=int(x),
                                  y_position=int(y),
                                  direction_view=Direction(direction),
                                  limits=limits)
            stage = TranslatorStages.WAITING_FOR_ROVER_MOVEMENTS
        elif stage == TranslatorStages.WAITING_FOR_ROVER_MOVEMENTS:
            if current_rover is None:
                raise ValueError("Rover can not be None")
            movements = item
            for movement in movements:
                if movement == "L":
                    current_rover.turn_left()
                elif movement == "R":
                    current_rover.turn_right()
                elif movement == "M":
                    current_rover.move()
            result += f"{current_rover.x_position} {current_rover.y_position} {current_rover.direction_view.value}\n"
            current_rover = None
            stage = TranslatorStages.WAITING_FOR_ROVER_INITIAL_POSITION
    return result.strip()
