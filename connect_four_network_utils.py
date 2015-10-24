import socket
import connect_four_utils as utils
from collections import namedtuple


_Connection =  namedtuple('socket_connection',['socket','socket_input','socket_output'])


class InvalidServerResponse(Exception):
    pass

def connect_to_server() -> "connection":
    ''' Attempts a connection to the server '''
    host, port = _get_connection_info()
    if host and port:
        return  _open_connection(host,port)
    else:
        return None
    
def start_game(connection:"connection", username:str) -> bool:
    ''' Begins a game by contacting the server with required protocol information '''
    try:
        _write_to_server(connection,"I32CFSP_HELLO {}".format(username)) 

        if _read_from_server(connection) == "WELCOME {}".format(username):
            _write_to_server(connection,"AI_GAME")
        return True
    except InvalidServerResponse:   
        print("Closing connection: Invalid server response")
        _close_connection(connection)
        return False

def end_game(connection: 'connection') -> None:
    ''' Clean up connection '''
    _close_connection(connection)
    print('Connection closed!')
    
def get_username() -> str:
    ''' Validates input for a username input '''
    while True:
        print("Enter a username (no spaces):", end = ' ')
        username = input().split()
        if len(username) != 1:
            print("[Connect Four] Invalid username")
        else:
            return username[0]
        
        
def sync_move(connection: 'connection', action: str, col: int) -> ():
    ''' Communicates a move with the server '''
    try:
        result = None
        winner = None

        # Loop until we get a result after an OKAY or WINNER from the server
        while not result:
            response = _read_from_server(connection)

            # Execute actions based upon the current server state
            if response == "OKAY":
                response = _read_from_server(connection).split()
                result = utils.validate_user_input(response)
            elif response == "READY":
                _write_to_server(connection,"{} {}".format(action, str(col + 1)))
            elif response == "INVALID":
                raise InvalidServerResponse
            elif response.startswith("WINNER"):
                result = namedtuple('Result', ['action', 'col', 'winner'])
                result.winner = response.split("_")[1]
            else:
                raise InvalidServerResponse

        return result
        
    except InvalidServerResponse:
        print("Invalid Server response")
        return None

def _get_connection_info() -> (str,int):
    ''' Get information from the user to connect to the server '''
    host = ''
    port = 0
    try:
        print("Input a hostname or ip:",end=' ')
        host = input()

        print("Input a port number [0-65535]:",end='  ')
        port = int(input())

        if port < 0 or port > 65535:
            raise ValueError
        else:
            return host, port
    except ValueError:
        print("Enter a valid input")
        return None, None
    
    
def _open_connection(host: str, port: int) -> "connection":
    ''' Connect to the server '''
    connection = socket.socket()
    try:
        connection.connect((host, port))
        con = _Connection(connection, connection.makefile('r'), connection.makefile('w'))
        return con
    except Exception:
        print("Could not connect to host: {}:{}".format(host,port))

        
def _close_connection(connection:"connection") -> None:
    ''' Clean up connection information '''
    connection.socket_input.close()
    connection.socket_output.close()
    connection.socket.close()

    
def _read_from_server(connection: _Connection) -> str:
    ''' Read line from the server '''
    return connection.socket_input.readline()[:-1]


def _write_to_server(connection: _Connection,message:str) -> None:
    ''' Write a line to the server '''
    connection.socket_output.write('{}\r\n'.format(message))
    connection.socket_output.flush()
