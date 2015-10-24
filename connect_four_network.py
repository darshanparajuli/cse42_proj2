# Anthony Lam 77341985
# Darshan Parajuli 16602518
# ICS 32 Fall 2015
# Project 2

import connect_four_network_utils as net_utils
import connectfour as game
import connect_four_utils as utils
from collections import namedtuple
import random 

# Test code
# import time, calendar

def get_random_move() -> '(action, col, winner)':
    ''' A test AI to play moves agains a remote server '''
    result = namedtuple('Result', ['action', 'col', 'winner'])
    result.col = random.randint(0, game.BOARD_COLUMNS - 1)
    if random.randint(0, 100) > 30:
        result.action = utils.ACTION_DROP
    else:
        result.action = utils.ACTION_POP
    result.winner = None
    return result
    

def main() -> None:
    # Connect to server
    while True:                 
        connection = net_utils.connect_to_server()
        if connection != None:
            user = net_utils.get_username()
            if net_utils.start_game(connection, user):                
                break
            else:
                return

    # Test code
    #connection = net_utils._open_connection("woodhouse.ics.uci.edu", 4444)
    #user = "batman"
    #net_utils.start_game(connection, user)
    #random.seed(calendar.timegm(time.gmtime()))
    
    # Variable Initialization
    winner = game.NONE
    players = ("RED", "YELLOW")
    player_names = {"RED": user, "YELLOW": "Server AI"}
    server_turn = False
    player_move = None

    input_format = "[{{}}] {}:".format(user)
    utils.print_instructions()
    game_state = game.new_game()

    while winner == game.NONE:
        utils.print_board(game_state.board)

        # Receive player moves and execute server side
        if not server_turn:
            # Test bot code
            #player_move = get_random_move()
            player_move = utils.get_input(game_state,players[server_turn], input_format)
        else:
            player_move = net_utils.sync_move(connection, player_move.action, player_move.col)
            print('[{}] {}: {} {}'.format(players[server_turn], \
                                          player_names[players[server_turn]], \
                                          player_move.action.title(), \
                                          (player_move.col + 1)))

        # Execute player moves
        try:
            game_state = utils.execute_move(game_state,player_move)
            winner = game.winner(game_state)
        except game.InvalidMoveError:
            print("[Connect Four] Invalid move")
            continue

        server_turn = not server_turn

    # Sync final moves to server and validate
    #  the winner remotely and locally
    player_move = net_utils.sync_move(connection, player_move.action, player_move.col)
    utils.print_board(game_state.board)
    _validate_winner(players[winner-1],player_move.winner,player_names)

    net_utils.end_game(connection)


def _validate_winner(local,server,names) -> None:
    ''' Ensures that the local and server winners are the same '''
    if local == server:
        print("[{}] {} WINS!!!".format(server, names[server]))
    else:
        print("Winner mismatch, someone cheated!")
    
if __name__ == "__main__":
    main()
    
