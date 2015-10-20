import connect_four_network_utils as net_utils
import connectfour as game
import connect_four_utils as utils


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
    
    print("Game Started")
    utils.print_instructions()
    game_state = game.new_game()

    winner = game.NONE
    players = ("RED","SERVER")
    i = 0

    player_move = None
    while True:
        utils.print_board(game_state.board)
        if i == 0:
            player_move = utils.get_input(players[i])
        else:
            player_move = net_utils.sync_move(connection, player_move.action, player_move.col)
            if player_move == None:
                break
        try:
            if player_move.action == utils.ACTION_POP:
                game_state = game.pop(game_state, player_move.col)
            else:
                game_state = game.drop(game_state, player_move.col)

            if player_move.winner != None:
                utils.print_board(game_state.board)
                print("Winner is: {}".format(player_move.winner))
                break
        except game.InvalidMoveError:
            print("Invalid move")
            continue

        i = (i + 1) % 2

    net_utils.end_game(connection)

if __name__ == "__main__":
    main()
    
