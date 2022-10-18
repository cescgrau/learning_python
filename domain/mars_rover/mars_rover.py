from domain.mars_rover.direction import Direction
from domain.mars_rover.grid_limits import GridLimits


class Rover:
    def __init__(self, x_position: int, y_position: int, direction_view: Direction, limits: GridLimits):
        if limits is None:
            raise ValueError("Limits is None")
        self.limits = limits
        self.direction_view = direction_view
        self.x_position = x_position
        self.y_position = y_position

    def move(self):
        if self.direction_view == Direction.N:
            if self.limits.y > self.y_position:
                self.y_position += 1
        elif self.direction_view == Direction.E:
            if self.limits.x > self.x_position:
                self.x_position += 1
        elif self.direction_view == Direction.S:
            if self.y_position > 0:
                self.y_position -= 1
        elif self.direction_view == Direction.W:
            if self.x_position > 0:
                self.x_position -= 1

    def turn_right(self):
        if self.direction_view == Direction.N:
            self.direction_view = Direction.E
        elif self.direction_view == Direction.E:
            self.direction_view = Direction.S
        elif self.direction_view == Direction.S:
            self.direction_view = Direction.W
        elif self.direction_view == Direction.W:
            self.direction_view = Direction.N

    def turn_left(self):
        if self.direction_view == Direction.N:
            self.direction_view = Direction.W
        elif self.direction_view == Direction.E:
            self.direction_view = Direction.N
        elif self.direction_view == Direction.S:
            self.direction_view = Direction.E
        elif self.direction_view == Direction.W:
            self.direction_view = Direction.S
