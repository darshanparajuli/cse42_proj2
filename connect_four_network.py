import connect_four_network_utils as net_utils
import connectfour as game
import connect_four_utils as utils

def main() -> None:
    is_connected = False
    connection = net_utils.connect_to_server()
    user = net_utils.get_username()
    is_connected = net_utils.start_game(connection,user)

    print("Game Started")
    utils.print_instructions()
    game_state = game.new_game()

    winner = game.NONE
    players = ("RED","SERVER")
    i = 0

    while is_connected:
        #Play our game
        utils.print_board(game_state.board)
        if i == 0:
            player_move = utils.get_input(players[i])
        else:
            player_move = sync_move(connection,player_move.action,player_move.col)
        try:
            if player_move.action == utils.ACTION_POP:
                game_state = game.pop(game_state, player_move.col)
            else:
                game_state = game.drop(game_state, player_move.col)

            send_move(connection,player_move.action,player_move.col)

        except:
            continue

        i = (i+1) % 2

if __name__ == "__main__":
    main()
    
