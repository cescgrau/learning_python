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
        self.stage = GameStage.WIP
        self.next_player = GamePlayers.PLAYER_X

    def get_tableau(self):
        return self.tableau

    def shot(self, player: GamePlayers, row, column):
        if self.stage != GameStage.WIP:
            raise RuntimeError()
        if self.next_player != player:
            raise RuntimeError()
        if player == GamePlayers.PLAYER_X:
            if self.tableau[row, column] is None:
                self.tableau[row, column] = "X"
                self.next_player = GamePlayers.PLAYER_Y
        if player == GamePlayers.PLAYER_Y:
            if self.tableau[row, column] is None:
                self.tableau[row, column] = "Y"
                self.next_player = GamePlayers.PLAYER_X
        self.stage = self.calculate_stage()
        return self.next_player

    def winner(self):
        if self.tableau.who_is_the_winner() == "X":
            return GamePlayers.PLAYER_X
        elif self.tableau.who_is_the_winner() == "Y":
            return GamePlayers.PLAYER_Y
        elif self.tableau.who_is_the_winner() is None:
            return None

    def calculate_stage(self):
        if self.tableau.is_full():
            return GameStage.OVER
        elif self.tableau.who_is_the_winner() is not None:
            return GameStage.OVER
        else:
            return GameStage.WIP
