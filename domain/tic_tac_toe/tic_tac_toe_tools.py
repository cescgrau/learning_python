from typing import Union, List, Optional, Tuple

PlayerId = str
Cell = Union[None, PlayerId]


def build_default_tableau() -> List[List[Cell]]:
    return [[None, None, None], [None, None, None], [None, None, None]]


class Tableau:
    def __init__(self, initial_value: Optional[List[List[Cell]]] = None) -> object:
        self.contents: List[
            List[Union[PlayerId, None]]] = build_default_tableau() if initial_value is None else initial_value

    def __getitem__(self, key: Tuple[int, int]) -> Cell:
        x = key[0]
        y = key[1]
        return self.contents[x][y]

    def __setitem__(self, key: Tuple[int, int], value: Cell):
        x = key[0]
        y = key[1]
        self.contents[x][y] = value

    def __str__(self) -> str:
        return str(self.contents)

    def __repr__(self) -> str:
        return str(self.contents)

    def __eq__(self, other):
        if not isinstance(other, List):
            raise ValueError("Can only compare with List")
        return self.contents == other

    def is_full(self) -> bool:
        for column in self.contents:
            for cell in column:
                if cell is None:
                    return False
        return True

    def who_is_the_winner(self) -> Union[PlayerId, None]:
        if self[0, 0] == self[0, 1] == self[0, 2] != 0:
            return self[0, 0]
        elif self[1, 0] == self[1, 1] == self[1, 2] != 0:
            return self[1, 0]
        elif self[2, 0] == self[2, 1] == self[2, 2] != 0:
            return self[2, 1]
        elif self[0, 0] == self[1, 0] == self[2, 0] != 0:
            return self[0, 0]
        elif self[0, 1] == self[1, 1] == self[2, 1] != 0:
            return self[0, 1]
        elif self[0, 2] == self[1, 2] == self[2, 2] != 0:
            return self[0, 2]
        elif self[0, 0] == self[1, 1] == self[2, 2] != 0:
            return self[0, 0]
        elif self[2, 0] == self[1, 1] == self[0, 2] != 0:
            return self[2, 0]
        return None


def review_tableau(tableau: Tableau) -> Union[None, PlayerId]:
    if tableau[0, 0] == tableau[0, 1] == tableau[0, 2] != 0:
        return tableau[0][0]
    elif tableau[1][0] == tableau[1][1] == tableau[1][2] != 0:
        return tableau[1][0]
    elif tableau[2][0] == tableau[2][1] == tableau[2][2] != 0:
        return tableau[2][1]
    elif tableau[2][1] == tableau[2][2] == tableau[2][2] != 0:
        return tableau[2][1]
    elif tableau[0][0] == tableau[1][0] == tableau[2][0] != 0:
        return tableau[0][0]
    elif tableau[0][1] == tableau[1][1] == tableau[2][1] != 0:
        return tableau[0][1]
    elif tableau[0][2] == tableau[1][2] == tableau[2][2] != 0:
        return tableau[0][2]
    elif tableau[0][0] == tableau[1][1] == tableau[2][2] != 0:
        return tableau[0][0]
    elif tableau[2][0] == tableau[1][1] == tableau[0][2] != 0:
        return tableau[2][0]
    return None


def player_shot(tableau: Tableau, player, row, column) -> Tableau:
    player_in_action(tableau, player, column, row)
    review_tableau(tableau)
    return tableau


def player_in_action(tableau: Tableau, player: PlayerId, column, row):
    if player == "player_x":
        if tableau.contents[row][column] is None:
            tableau.contents[row][column] = "X"
    if player == "player_y":
        if tableau.contents[row][column] is None:
            tableau.contents[row][column] = "Y"
    return tableau
