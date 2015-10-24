# -*- coding: utf-8 -*-

import connectfour
from collections import namedtuple


'''Actions'''
ACTION_DROP = 'DROP'
ACTION_POP = 'POP'

_BORDER_CHAR = u'\u25A0'
    
def print_instructions() -> None:
    ''' Print instructions '''
    print()
    print("Welcome to the best Connect Four game ever made!!!")
    print("Instructions:")
    print("  1. You can either drop your piece or pop your piece.")
    print("  2. To drop, enter 'drop column#', i.e. 'drop 4'.")
    print("  3. Top pop, enter 'pop column#', i.e. 'pop 3'.")
    
def execute_move(game_state,player_move) -> 'game_state':
    ''' Performs a local move based on a player action '''
    if player_move.action == ACTION_POP:
        return game.pop(game_state, player_move.col)
    elif player_move.action == ACTION_DROP:
        return game.drop(game_state, player_move.col)

def print_board(game_board: [str]) -> None:
    ''' Print board '''
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

    # Loop through rows and columns to print the list of characters
    for i in range(connectfour.BOARD_ROWS):
        print("{}".format(_BORDER_CHAR).ljust(max_digit_len), end=' ')
        for j in range(connectfour.BOARD_COLUMNS + 1):
            if j == connectfour.BOARD_COLUMNS:
                print("{}".format(_BORDER_CHAR).ljust(max_digit_len), end=' ')
            else:
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

    for i in range(0, connectfour.BOARD_COLUMNS + 2):
        print("{}".format(_BORDER_CHAR).ljust(max_digit_len), end=' ')

    print()
    print()
    
    
def get_input(game_state: 'GameState' ,cur_player: str, input_format = "Player {}'s turn:") -> ():
    ''' Gets the user input '''
    while True:
        print(input_format.format(cur_player),end=' ')
        value_input = input().split()
        result = validate_user_input(value_input)
        if result != None:
            return result
        
        print("[Connect Four] Invalid move")
        print_board(game_state.board)

def validate_user_input(user_input: [str]) -> bool:
    ''' Validates user input to determine if it's within required boundaries '''
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
