import socket
import connect_four_utils as utils
from collections import namedtuple

_EOL = "\r\n"

_Connection =  namedtuple('socket_connection',['socket','socket_input','socket_output'])

class InvalidServerResponse(Exception):
    pass

def _get_connection_info() -> (str,int):
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
            return host,port
    except ValueError:
        print("Enter a valid input")


def _open_connection(host: str, port: int) -> "connection":
    server = socket.socket()
    try:
        server.connect((host,port))
        con = _Connection(server,server.makefile('r'),server.makefile('w'))
        return con
    except Exception:
        print("Could not connect to host: {}:{}".format(host,port))

def connect_to_server() -> "connection":
    host,port = _get_connection_info()
    return  _open_connection(host,port)

def start_game(server:"connection",username:str) -> bool:
    try:
        _write_to_server(server,"I32CFSP_HELLO {}".format(username)) 

        if _read_from_server(server) == "WELCOME {}".format(username):
            _write_to_server(server,"AI_GAME")
        else:
            raise InvalidServerException
        if _read_from_server(server) != "READY":
            raise InvalidServerException
        return True

    except InvalidServerException:   
        print("Closing connection: Invalid server response")
        _close_connection(server)
        return False

def get_username() -> str:
    while True:
        print("Enter a username: (no spaces)")
        username = input().split()
        if len(username) != 1:
            print("Invalid username")
        else:
            return username[0]

def sync_move(server:_Connection,action:str,col:int) -> ():
    try:
        if _read_from_server(server) != "READY":
            raise InvalidServerResponse

        _write_to_server(server,action + str(col))
        if _read_from_server(server) == "OKAY":
            result = namedtuple('Result', ['action', 'col'])
            response = _read_from_server(server).split()
            result.action = response[0]
            result.col = int(response[1])
            return result
        else:
            raise InvalidServerResponse
    except InvalidServerResponse:
        print("Invalid Server response")


def _close_connection(server:"connection") -> None:
    server.socket_input.close()
    server.socket_output.close()
    server.socket.close()

def _read_from_server(server: _Connection) -> str:
    return server.socket_input.readline()[:-1]

def _write_to_server(server: _Connection,message:str) -> None:
    server.socket_output.write(message + _EOL)
    server.socket_output.flush()
    

