import connect_four_network_utils as net_utils
import connectfour as game
import connect_four_utils as utils
import random, time, calendar
from collections import namedtuple

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

    # Test connection
    #connection = net_utils._open_connection("woodhouse.ics.uci.edu", 4444)
    #user = "batman"
    #net_utils.start_game(connection, user)
    #random.seed(calendar.timegm(time.gmtime()))
    

    # Variable Initialization
    winner = game.NONE
    players = ("RED", "YELLOW")
    player_names = {"RED": user, "YELLOW": "Server AI"}
    is_server = False
    player_move = None

    input_format = "[{{}}] {}: ".format(user)
    utils.print_instructions()
    game_state = game.new_game()

    while winner == game.NONE:
        utils.print_board(game_state.board)

        # Receive player moves and execute server side
        if not is_server:
            # Test bot code
            #player_move = get_random_move()
            player_move = utils.get_input(game_state,players[is_server], input_format)
        else:
            player_move = net_utils.sync_move(connection, player_move.action, player_move.col)

        print('[{}] {}: {} {}'.format(\
            players[is_server],\
            player_names[players[is_server]],\
            player_move.action.title(),\
            (player_move.col + 1)))
        # Execute player moves locally
        try:
            game_state = execute_move(game_state,player_move)
            winner = game.winner(game_state)

        except game.InvalidMoveError:
            print("[Connect Four] Invalid move")
            continue

        is_server = not is_server

    # Sync final moves to server and validate
    #  the winner remotely and locally
    player_move = net_utils.sync_move(connection, player_move.action, player_move.col)
    utils.print_board(game_state.board)
    validate_winner(players[winner-1],player_move.winner,player_names)

    net_utils.end_game(connection)
    time.sleep(1)

def execute_move(game_state,player_move) -> 'game_state':
    ''' Performs a local move based on a player action '''
    if player_move.action == utils.ACTION_POP:
        return game.pop(game_state, player_move.col)
    elif player_move.action == utils.ACTION_DROP:
        return game.drop(game_state, player_move.col)

def validate_winner(local,server,names) -> None:
    ''' Ensures that the local and server winners are the same '''
    if local == server:
        print("[{}] {} WINS!!!".format(server, names[server]))
    else:
        print("Winner mismatch, someone cheated!")
    
if __name__ == "__main__":
    main()
    
