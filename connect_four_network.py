import connect_four_network_utils as net_utils
import connect_four_utils as utils

def main() -> None:
    is_connected = False
    connection = net_utils.connect_to_server()
    user = net_utils.get_username()
    is_connected = net_utils.start_game(connection,user)
    print("Game Started")
    utils.print_instructions()

    while is_connected:
        #Play our game
        utils.print_board()





if __name__ == "__main__":
    main()
    
