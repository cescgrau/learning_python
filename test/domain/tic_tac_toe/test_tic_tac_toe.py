import unittest
from typing import Union, List


def build_default_tableau() -> List:
    return [[None, None, None], [None, None, None], [None, None, None]]


PlayerId = str


class Tableau:
    def __init__(self):
        self.contents: List[List[Union[PlayerId, None]]] = build_default_tableau()


def review_tableau(tableau: List) -> Union[None, PlayerId]:
    if tableau[0][0] == tableau[0][1] == tableau[0][2] != 0:
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
    review_tableau(tableau.contents)
    return tableau


def player_in_action(tableau: Tableau, player: PlayerId, column, row):
    if player == "player_x":
        if tableau.contents[row][column] is None:
            tableau.contents[row][column] = "X"
    if player == "player_y":
        if tableau.contents[row][column] is None:
            tableau.contents[row][column] = "Y"
    return tableau


class TicTacToeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tableau = Tableau()

    def test_introducing__a_shot_for_player_x(self):
        self.assertEqual([[None, None, None], [None, "X", None], [None, None, None]],
                         player_shot(self.tableau, "player_x", 1, 1).contents)

    def test_introducing__a_shot_for_player_y(self):
        self.assertEqual([[None, None, None], [None, "X", None], [None, None, None]],
                         player_shot(self.tableau, "player_x", 1, 1).contents)
        self.assertEqual([[None, None, None], [None, "X", "Y"], [None, None, None]],
                         player_shot(self.tableau, "player_y", 1, 2).contents)

    def test_introducing__a_shot_for_player_x_y_x_y_x_win_x(self):
        self.assertEqual([[None, None, None], [None, "X", None], [None, None, None]],
                         player_shot(self.tableau, "player_x", 1, 1).contents)
        self.assertEqual([[None, None, None], [None, "X", "Y"], [None, None, None]],
                         player_shot(self.tableau, "player_y", 1, 2).contents)
        self.assertEqual([[None, "X", None], [None, "X", "Y"], [None, None, None]],
                         player_shot(self.tableau, "player_x", 0, 1).contents)
        self.assertEqual([[None, "X", "Y"], [None, "X", "Y"], [None, None, None]],
                         player_shot(self.tableau, "player_y", 0, 2).contents)
        self.assertEqual([[None, "X", "Y"], [None, "X", "Y"], [None, "X", None]],
                         player_shot(self.tableau, "player_x", 2, 1).contents)

    def test_introducing__a_shot_for_player_x_y_x_y_x_y_win_y(self):
        self.assertEqual([[None, None, None], [None, "X", None], [None, None, None]],
                         player_shot(self.tableau, "player_x", 1, 1).contents)
        self.assertEqual([[None, None, None], [None, "X", "Y"], [None, None, None]],
                         player_shot(self.tableau, "player_y", 1, 2).contents)
        self.assertEqual([[None, "X", None], [None, "X", "Y"], [None, None, None]],
                         player_shot(self.tableau, "player_x", 0, 1).contents)
        self.assertEqual([[None, "X", "Y"], [None, "X", "Y"], [None, None, None]],
                         player_shot(self.tableau, "player_y", 0, 2).contents)
        self.assertEqual([[None, "X", "Y"], [None, "X", "Y"], ["X", None, None]],
                         player_shot(self.tableau, "player_x", 2, 0).contents)
        self.assertEqual([[None, "X", "Y"], [None, "X", "Y"], ["X", None, "Y"]],
                         player_shot(self.tableau, "player_y", 2, 2).contents)


if __name__ == '__main__':
    unittest.main()
