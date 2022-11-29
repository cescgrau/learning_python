from enum import Enum

from domain.tic_tac_toe.tic_tac_toe_tools import Tableau, review_tableau, player_shot


class GameStage(Enum):
    WIP = 1
    OVER = 2


class GamePlayers(Enum):
    PLAYER_X = 1
    PLAYER_Y = 2


class TicTacToeGame:

    def __init__(self, tableau: Tableau):
        self.tableau = tableau


    def get_tableau(self):
        return self.tableau

    def shot(self, player: str, row, column):
        if player == "player_x":
            if self.tableau[row, column] is None:
                self.tableau[row, column] = "X"
                return GamePlayers.PLAYER_Y
        if player == "player_y":
            if self.tableau[row, column] is None:
                self.tableau[row, column] = "Y"
                return GamePlayers.PLAYER_X

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
