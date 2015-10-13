import connectfour
import connect_four_utils as utils


def main() -> None:
    pass


def print_instructions() -> None:
    print("Type in column number to drop your piece")
    print("For example, to drop a piece at sixth column, type '6'")
    print("Type in column number prefixed by letter p to pop the bottom piece")
    print("For example, 'p6' will pop the bottom piece at sixth column")
    print()

def test() -> None:
    print_instructions()
    
    game_state = connectfour.new_game()
    utils.print_board(game_state[utils.BOARD])

    winner = connectfour.NONE
    players = ("RED", "YELLOW")
    i = 0
    
    while True:
        player_move = utils.get_input(players[i])
        try:
            if player_move["pop"]:
                game_state = connectfour.pop(game_state,player_move["col"])
            else:
                game_state = connectfour.drop(game_state, player_move["col"])
        except connectfour.InvalidMoveError:
            print("invalid move")
            continue

        utils.print_board(game_state[utils.BOARD])
        i = (i + 1) % 2

        winner = connectfour.winner(game_state)
        if winner != connectfour.NONE:
            break

    print('winner: {}'.format(winner))

if __name__ == "__main__":
    test()
    #main()
