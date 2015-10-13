import connectfour
import connect_four_utils as utils


def main() -> None:
    pass


def test() -> None:
    game_state = connectfour.new_game()
    player_move = utils.get_input("RED")
    game_state = connectfour.drop(game_state, player_move)
    utils.print_board(game_state[utils.BOARD])
    player_move = utils.get_input("YELLOW")
    game_state = connectfour.drop(game_state, player_move)
    utils.print_board(game_state[utils.BOARD])


if __name__ == "__main__":
    test()
    #main()
