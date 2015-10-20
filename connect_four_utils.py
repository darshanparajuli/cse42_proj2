# -*- coding: utf-8 -*-

import connectfour
from collections import namedtuple


'''Actions'''
ACTION_DROP = 'DROP'
ACTION_POP = 'POP'

_BORDER_CHAR = u'\u25A0'
    
def print_instructions() -> None:
    print("To drop: drop col#")
    print("To pop:  pop col#")

    
def print_board(game_board: [str]) -> None:
    max_digit_len = len(str(connectfour.BOARD_COLUMNS))

    print()
    for i in range(0, connectfour.BOARD_COLUMNS + 2):
        print("{}".format(_BORDER_CHAR).ljust(max_digit_len), end=' ')
    print()
    
    for i in range(0, connectfour.BOARD_COLUMNS + 2):
        temp = None
        if i == 0 or i == connectfour.BOARD_COLUMNS + 1:
            temp = _BORDER_CHAR
        else:
            temp = str(i)            
        print("{}".format(temp).ljust(max_digit_len), end=' ')
    print()

    for i in range(connectfour.BOARD_ROWS):
        print("{}".format(_BORDER_CHAR).ljust(max_digit_len), end=' ')
        for j in range(connectfour.BOARD_COLUMNS + 1):
            if j == connectfour.BOARD_COLUMNS:
                print("{}".format(_BORDER_CHAR).ljust(max_digit_len), end=' ')
            else:
                piece = game_board[j][i]
                printable_piece = None
                if piece == connectfour.NONE:
                    printable_piece = u'\u25CB'
                elif piece == connectfour.RED:
                    printable_piece = 'R'
                elif piece == connectfour.YELLOW:
                    printable_piece = 'Y'
                if printable_piece != None:
                    print(printable_piece.ljust(max_digit_len), end=' ')
        print()

    for i in range(0, connectfour.BOARD_COLUMNS + 2):
        print("{}".format(_BORDER_CHAR).ljust(max_digit_len), end=' ')

    print()
    print()
    
    
def get_input(cur_player:str) -> ():
    ''' Gets the user input as an integer only '''
    while True:
        print("Player {}'s turn:".format(cur_player),end=' ')
        value_input = input().split()

        result = validate_user_input(value_input)
        if result != None:
            return result
        
        print('invalid input')

def validate_user_input(user_input: [str]) -> bool:
    if len(user_input) == 2:
        action = user_input[0].upper()
        column = user_input[1]
    
        if (action == ACTION_DROP or action == ACTION_POP) and column.isdigit():
            column = int(column)
            if column >= 1 and column <= connectfour.BOARD_COLUMNS:
                result = namedtuple('Result', ['action', 'col', 'winner'])
                result.action = action
                result.col = column - 1
                result.winner = None
                return result
    return None
