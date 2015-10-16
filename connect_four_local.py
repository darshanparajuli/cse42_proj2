import connectfour as connectfour_base
import connect_four_utils as utils


def test() -> None:
    pass


def run_game() -> None:
    utils.print_instructions()
    
    game_state = connectfour_base.new_game()
    
    winner = connectfour_base.NONE
    players = ("RED", "YELLOW")
    i = 0
    
    while True:
        utils.print_board(game_state.board)
        player_move = utils.get_input(players[i])
        try:
            if player_move.action == utils.ACTION_POP:
                game_state = connectfour_base.pop(game_state, player_move.col)
            else:
                game_state = connectfour_base.drop(game_state, player_move.col)
        except connectfour_base.InvalidMoveError:
            continue

        i = (i + 1) % 2

        winner = connectfour_base.winner(game_state)
        if winner != connectfour_base.NONE:
            break

    winner_name = 'NONE'
    if winner == connectfour_base.RED:
        winner_name = 'RED'
    elif winner == connectfour_base.YELLOW:
        winner_name = 'YELLOW'

    print('winner: {}'.format(winner_name))

    
if __name__ == "__main__":
    #test()
    run_game()
