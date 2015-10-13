import connectfour
import connect_four_utils as utils


def main() -> None:
    pass


def test() -> None:
    game_state = connectfour.new_game()
    game_state = connectfour.drop(game_state, 4)
    game_state = connectfour.drop(game_state, 2)
    utils.print_board(game_state[utils.BOARD])


if __name__ == "__main__":
    test()
    #main()
