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


def specific_player():

    context = zmq.Context()

    player = input("Enter player name:")

    print("Connecting to NBA player server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    print(f"Sending request...")
    socket.send_string(player)

    # receive serialized data (JSON) from microservice
    player_data = json.loads(socket.recv())

    # TO DO: implement error message (player not found)

    print(tabulate([data for data in player_data.items()], tablefmt="psql"))
    print("\n")


def random_player():

    context = zmq.Context()

    print("Connecting to NBA player server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    print(f"Sending request...")
    socket.send_string("random")

    # receive serialized data (JSON) from microservice
    rand_player = socket.recv()

    print(rand_player)
    print("\n")