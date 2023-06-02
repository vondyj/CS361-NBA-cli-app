import json
import zmq

from InquirerPy import inquirer
from tabulate import tabulate


def players_menu():

    # will be displayed until the user selects "Main menu"
    while True:
        menu = inquirer.select(
            message="Player Options:",
            choices=["Get information about a specific player",
                     "Get a random player",
                     "Main menu"]

        ).execute()

        match menu:
            case "Get information about a specific player":
                get_specific_player()
            case "Get a random player":
                get_random_player()
            case _:
                print("\n")
                return


def start_socket():

    # set up communication with NBA_Player_Microservice.py
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # return the socket to the method that called it
    return socket


def get_specific_player():

    socket = start_socket()

    # get user input
    user_input = input("Enter player name (partial names are searchable): ")

    # send request to NBA_Player_Microservice.py
    socket.send_string(user_input)

    # receive serialized data (JSON) from microservice
    player_data = json.loads(socket.recv())

    match player_data:
        case "ERROR: Invalid Search":
            print(f"\n{player_data}\n")
        case _:
            table_data = parse_player_data(player_data)
            print(tabulate(table_data, tablefmt="heavy_grid"))


def parse_player_data(data):

    name = data["first_name"] + " " + data["last_name"]
    team = data["team"]["full_name"]
    position = data["position"]

    match position:
        case "C":
            position = "Center"
        case "G":
            position = "Guard"
        case "F":
            position = "Forward"
        case "C-F":
            position = "Center Forward"
        case "F-C":
            position = "Forward Center"
        case "":
            position = "N/A"

    match data["height_feet"]:
        case None:
            height = "N/A"
        case _:
            height = str(data["height_feet"]) + " ft " + str(data["height_inches"]) + ' in'

    match data["weight_pounds"]:
        case None:
            weight = "N/A"
        case _:
            weight = str(data["weight_pounds"]) + " lbs"

    table_data = [["Name", name], ["Position", position], ["Team", team], ["Height", height], ["Weight", weight]]

    return table_data


def get_random_player():

    socket = start_socket()

    # send request to NBA_Player_Microservice.py
    socket.send_string("random")

    player = socket.recv_string()
    print(f"\n{player}\n")
