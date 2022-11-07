import unittest
from enum import Enum

from domain.tic_tac_toe.tic_tac_toe_tools import Tableau


class GameStage(Enum):
    WIP = 1
    OVER = 2


class TicTacToeGame:

    def __init__(self, tableau: Tableau):
        self.tableau = tableau

    def get_tableau(self):
        return self.tableau

    def shot(self, player, row, column):
        if player == "player_x":
            if self.tableau[row, column] is None:
                self.tableau[row, column] = "X"
        if player == "player_y":
            if self.tableau[row, column] is None:
                self.tableau[row, column] = "Y"

    def winner(self):
        if self.tableau.who_is_the_winner() == "X":
            return "player_x"
        elif self.tableau.who_is_the_winner() == "Y":
            return "player_y"
        elif self.tableau.who_is_the_winner() is None:
            return None

    def stage(self):
        if self.tableau.is_full():
            return GameStage.OVER
        elif self.tableau.who_is_the_winner() is not None:
            return GameStage.OVER
        else:
            return GameStage.WIP


class TestTicTacToeEvolution(unittest.TestCase):
    def test_from_empty_tableau_player_x_perform_first_shot(self):
        tableau = Tableau()
        player = "player_x"
        game = TicTacToeGame(tableau)
        game.shot(player, row=1, column=1)
        self.assertEqual([[None, None, None], [None, "X", None], [None, None, None]], game.get_tableau())

    def test_from_empty_tableau_to_end_game(self):
        tableau = Tableau()

        tableau1 = Tableau([[None]])
        tableau1.contents
        tableau2 = Tableau([[X]])
        player_x = "player_x"
        player_y = "player_y"
        game = TicTacToeGame(tableau)
        game.shot(player_x, row=1, column=1)
        self.assertEqual(GameStage.WIP, game.stage())
        game.shot(player_y, row=0, column=1)
        game.shot(player_x, row=0, column=0)
        game.shot(player_y, row=1, column=2)
        game.shot(player_x, row=2, column=2)
        self.assertEqual([["X", "Y", None], [None, "X", "Y"], [None, None, "X"]], game.get_tableau())
        self.assertEqual(player_x, game.winner())
        self.assertEqual(GameStage.OVER, game.stage())

    def test_from_empty_tableau_to_end_game_without_winner(self):
        tableau = Tableau()
        player_x = "player_x"
        player_y = "player_y"
        game = TicTacToeGame(tableau)
        game.shot(player_x, row=1, column=1)
        game.shot(player_y, row=0, column=0)
        game.shot(player_x, row=1, column=0)
        game.shot(player_y, row=0, column=1)
        game.shot(player_x, row=0, column=2)
        game.shot(player_y, row=2, column=0)
        game.shot(player_x, row=2, column=2)
        game.shot(player_y, row=1, column=2)
        game.shot(player_x, row=2, column=1)
        self.assertEqual([["Y", "Y", "X"], ["X", "X", "Y"], ["Y", "X", "X"]], game.get_tableau())
        self.assertEqual(None, game.winner())
        self.assertEqual(GameStage.OVER, game.stage())


        if __name__ == '__main__':
            unittest.main()
