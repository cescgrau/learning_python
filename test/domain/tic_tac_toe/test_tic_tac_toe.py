import unittest


def review_tableau(tableau):
    if tableau[0][0] == tableau[0][1] == tableau[0][2] != 0:
        print("win", tableau[0][0])
    elif tableau[1][0] == tableau[1][1] == tableau[1][2] != 0:
        print("win", tableau[1][0])
    elif tableau[2][0] == tableau[2][1] == tableau[2][2] != 0:
        print("win", tableau[2][1])
    elif tableau[2][1] == tableau[2][2] == tableau[2][2] != 0:
        print("win", tableau[2][1])
    elif tableau[0][0] == tableau[1][0] == tableau[2][0] != 0:
        print("win", tableau[0][0])
    elif tableau[0][1] == tableau[1][1] == tableau[2][1] != 0:
        print("win", tableau[0][1])
    elif tableau[0][2] == tableau[1][2] == tableau[2][2] != 0:
        print("win", tableau[0][2])
    elif tableau[0][0] == tableau[1][1] == tableau[2][2] != 0:
        print("win", tableau[0][0])
    elif tableau[2][0] == tableau[1][1] == tableau[0][2] != 0:
        print("win", tableau[2][0])


def player_shot(tableau, player, row, column):
    player_in_action(tableau, player, column, row)
    review_tableau(tableau)
    return tableau


def player_in_action(tableau, player, column, row):
    if player == "player_x":
        if tableau[row][column] == 0:
            tableau[row][column] = "X"
    if player == "player_y":
        if tableau[row][column] == 0:
            tableau[row][column] = "Y"
    return tableau


class TicTacToeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tableau = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def test_introducing__a_shot_for_player_x(self):
        self.assertEqual([[0, 0, 0], [0, "X", 0], [0, 0, 0]], player_shot(self.tableau, "player_x", 1, 1))

    def test_introducing__a_shot_for_player_y(self):
        self.assertEqual([[0, 0, 0], [0, "X", 0], [0, 0, 0]], player_shot(self.tableau, "player_x", 1, 1))
        self.assertEqual([[0, 0, 0], [0, "X", "Y"], [0, 0, 0]], player_shot(self.tableau, "player_y", 1, 2))

    def test_introducing__a_shot_for_player_x_y_x_y_x_win_x(self):
        self.assertEqual([[0, 0, 0], [0, "X", 0], [0, 0, 0]], player_shot(self.tableau, "player_x", 1, 1))
        self.assertEqual([[0, 0, 0], [0, "X", "Y"], [0, 0, 0]], player_shot(self.tableau, "player_y", 1, 2))
        self.assertEqual([[0, "X", 0], [0, "X", "Y"], [0, 0, 0]], player_shot(self.tableau, "player_x", 0, 1))
        self.assertEqual([[0, "X", "Y"], [0, "X", "Y"], [0, 0, 0]], player_shot(self.tableau, "player_y", 0, 2))
        self.assertEqual([[0, "X", "Y"], [0, "X", "Y"], [0, "X", 0]], player_shot(self.tableau, "player_x", 2, 1))

    def test_introducing__a_shot_for_player_x_y_x_y_x_y_win_y(self):
        self.assertEqual([[0, 0, 0], [0, "X", 0], [0, 0, 0]], player_shot(self.tableau, "player_x", 1, 1))
        self.assertEqual([[0, 0, 0], [0, "X", "Y"], [0, 0, 0]], player_shot(self.tableau, "player_y", 1, 2))
        self.assertEqual([[0, "X", 0], [0, "X", "Y"], [0, 0, 0]], player_shot(self.tableau, "player_x", 0, 1))
        self.assertEqual([[0, "X", "Y"], [0, "X", "Y"], [0, 0, 0]], player_shot(self.tableau, "player_y", 0, 2))
        self.assertEqual([[0, "X", "Y"], [0, "X", "Y"], ["X", 0, 0]], player_shot(self.tableau, "player_x", 2, 0))
        self.assertEqual([[0, "X", "Y"], [0, "X", "Y"], ["X", 0, "Y"]], player_shot(self.tableau, "player_y", 2, 2))


if __name__ == '__main__':
    unittest.main()
