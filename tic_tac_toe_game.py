
from domain.tic_tac_toe.tic_tac_toe_tools import Tableau, player_in_action
from domain.tic_tac_toe.tic_tac_toe_evolution import TicTacToeGame, GamePlayers, GameStage

the_game=TicTacToeGame(tableau=Tableau())

while the_game.stage == GameStage.WIP:
    print(the_game.next_player)
    print("Enter your Coord X:")
    x = int(input())
    print("Enter your Coord Y:")
    y = int(input())
    print("Your shot is:", x, ",", y)
    the_game.shot(the_game.next_player, x, y)
    print(the_game.tableau)

print(f"the winner is: {the_game.winner()}")




