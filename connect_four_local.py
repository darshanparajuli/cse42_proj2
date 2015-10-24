# Anthony Lam 77341985
# Darshan Parajuli 16602518
# ICS 32 Fall 2015
# Project 2

import connectfour as game
import connect_four_utils as utils


def run_game() -> None:
    ''' Starts a local game '''
    utils.print_instructions()
    game_state = game.new_game()
    
    winner = game.NONE
    players = ("RED", "YELLOW")
    yellow_turn =  False
    
    while winner == game.NONE:
        utils.print_board(game_state.board)
        player_move = utils.get_input(game_state,players[yellow_turn])
        
        # Select a player action 
        try:
            game_state = utils.execute_move(game_state,player_move)
        except game.InvalidMoveError:
            print("[Connect Four] Invalid move")
            continue

        # Swap players
        yellow_turn = not yellow_turn

        winner = game.winner(game_state)

    utils.print_board(game_state.board)

    winner_name = 'NONE'
    if winner == game.RED:
        winner_name = 'RED'
    elif winner == game.YELLOW:
        winner_name = 'YELLOW'

    print('[Connect Four] Winner: {}'.format(winner_name))

    
if __name__ == "__main__":
    run_game()
