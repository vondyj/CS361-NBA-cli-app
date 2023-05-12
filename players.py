import json
import zmq

from InquirerPy import inquirer
from tabulate import tabulate


def players_menu():

    # will run until the user selects "Main menu"
    while True:
        menu = inquirer.select(
            message="Player Options:",
            choices=["Get stats for a specific player",
                     "Get a random player",
                     "Main menu"]

        ).execute()

        if menu == "Get stats for a specific player":
            specific_player()
        elif menu == "Get a random player":
            random_player()
        else:
            print("\n")
            break


def start_socket():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    return socket


def specific_player():

    socket = start_socket()
    user_input = input("Enter player name: ")

    # send request to NBA_Player_Microservice.py
    socket.send_string(user_input)

    # receive serialized data (JSON) from microservice
    player_data = json.loads(socket.recv())

    # pretty print (for display purposes only)
    print(json.dumps(player_data, indent=4))


def random_player():

    socket = start_socket()

    # send request to NBA_Player_Microservice.py
    socket.send_string("random")

    # receive response from NBA_Player_Microservice.py
    player = socket.recv_string()

    print(f"\n{player}\n")
