import connect_four_network_utils as net_utils
import connectfour as game
import connect_four_utils as utils

# TODO: remove these
import random
import time
import calendar
from collections import namedtuple

def get_random_move() -> '(action, col, winner)':
    result = namedtuple('Result', ['action', 'col', 'winner'])
    result.col = random.randint(0, game.BOARD_COLUMNS - 1)
    if random.randint(0, 100) > 30:
        result.action = utils.ACTION_DROP
    else:
        result.action = utils.ACTION_POP
    result.winner = None
    return result
    

def main() -> None:
    # while True:                 
    #     connection = net_utils.connect_to_server()
    #     if connection != None:
    #         user = net_utils.get_username()
    #         if net_utils.start_game(connection, user):                
    #             break
    #         else:
    #             return

    # TODO: remove these
    connection = net_utils._open_connection("woodhouse.ics.uci.edu", 4444)
    user = "batman"
    net_utils.start_game(connection, user)
    random.seed(calendar.timegm(time.gmtime()))
    
    utils.print_instructions()
    game_state = game.new_game()

    winner = game.NONE
    players = ("RED", "YELLOW")
    player_names = {"RED": user, "YELLOW": "Server AI"}
    is_server = False

    player_move = None
    input_format = "[{{}}] {}: ".format(user)
    while winner == game.NONE:
        utils.print_board(game_state.board)
        if not is_server:
            player_move = get_random_move() #utils.get_input(players[i], input_format)
            print('[{}] {}: {} {}'.format(players[is_server], user, player_move.action.title(), (player_move.col + 1)))
        else:
            player_move = net_utils.sync_move(connection, player_move.action, player_move.col)
            print('[{}] Server AI: {} {}'.format(players[is_server], player_move.action.title(), (player_move.col + 1)))
        try:
            if player_move.action == utils.ACTION_POP:
                game_state = game.pop(game_state, player_move.col)
            elif player_move.action == utils.ACTION_DROP:
                game_state = game.drop(game_state, player_move.col)

            winner = game.winner(game_state)

        except game.InvalidMoveError:
            print("Invalid move")
            continue

        is_server = not is_server

    utils.print_board(game_state.board)
    print("[{}] {} WINS!!!".format(players[winner-1], player_names[players[winner-1]]))
    net_utils.end_game(connection)
    time.sleep(1)
    
if __name__ == "__main__":
    while True:
        main()
    
