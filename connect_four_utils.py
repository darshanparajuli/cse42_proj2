import connectfour

'''GameState tuple constants'''
BOARD = 0
TURN = 1

def print_board(game_board: [str]) -> None:
    for i in range(1, 8):
        print("{} ".format(str(i)), end='')
    print()

    for i in range(connectfour.BOARD_ROWS):
        for j in range(connectfour.BOARD_COLUMNS):
            piece = game_board[j][i]
            if piece == connectfour.NONE:
                print('.', end=' ')
            elif piece == connectfour.RED:
                print('R', end=' ')
            elif piece == connectfour.YELLOW:
                print('Y', end=' ')
            
        print()
    
