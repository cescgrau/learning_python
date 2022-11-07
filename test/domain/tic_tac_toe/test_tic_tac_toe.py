import unittest

from domain.tic_tac_toe.tic_tac_toe_tools import Tableau, player_shot


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
