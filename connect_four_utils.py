import connectfour

'''GameState tuple constants'''
BOARD = 0
TURN = 1

def print_board(game_board: [str]) -> None:
    max_digit_len = len(str(connectfour.BOARD_COLUMNS))

    for i in range(1, connectfour.BOARD_COLUMNS+1):
        print("{}".format(str(i)).ljust(max_digit_len), end=' ')
    print()

    for i in range(connectfour.BOARD_ROWS):
        for j in range(connectfour.BOARD_COLUMNS):
            piece = game_board[j][i]
            printable_piece = None
            if piece == connectfour.NONE:
                printable_piece = '.'
            elif piece == connectfour.RED:
                printable_piece = 'R'
            elif piece == connectfour.YELLOW:
                printable_piece = 'Y'
            if printable_piece != None:
                print(printable_piece.ljust(max_digit_len), end=' ')
        print()

def get_input(cur_player:str) -> int:
    ''' Gets the user input as an integer only '''
    while True:
        try:
            print("Enter a column {} player: ".format(cur_player),end='')
            value_input = int(input())      
            if _validate_input(value_input):
                return value_input-1 
            else:
                print("Column must be between 1 and {}".format(connectfour.BOARD_COLUMNS))
        except ValueError:
            print("Invalid column")

def _validate_input(test:int)-> bool:
    return test > 0 and test <= connectfour.BOARD_COLUMNS
