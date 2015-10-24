import connectfour as game
import connect_four_utils as utils


def run_game() -> None:
    ''' Starts a local game '''
    utils.print_instructions()
    game_state = game.new_game()
    
    winner = game.NONE
    players = ("RED", "YELLOW")
    i = 0
    
    while True:
        utils.print_board(game_state.board)
        player_move = utils.get_input(game_state,players[i])
        
        # Select a player action 
        try:
            if player_move.action == utils.ACTION_POP:
                game_state = game.pop(game_state, player_move.col)
            else:
                game_state = game.drop(game_state, player_move.col)
        except game.InvalidMoveError:
            print("Invalid move")
            continue

        # Swap players
        i = (i + 1) % 2

        winner = game.winner(game_state)
        if winner != game.NONE:
            break

    winner_name = 'NONE'
    if winner == game.RED:
        winner_name = 'RED'
    elif winner == game.YELLOW:
        winner_name = 'YELLOW'

    print('winner: {}'.format(winner_name))

    
if __name__ == "__main__":
    run_game()
