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

        if menu == "Get information about a specific player":
            specific_player()
        elif menu == "Get a random player":
            random_player()
        else:
            print("\n")
            return


def start_socket():

    # set up communication with NBA_Player_Microservice.py
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # return the socket to the method that called it
    return socket


def specific_player():

    socket = start_socket()

    # get user input
    user_input = input("Enter player name (partial names are searchable): ")

    # send request to NBA_Player_Microservice.py
    socket.send_string(user_input)

    # receive serialized data (JSON) from microservice
    player_data = json.loads(socket.recv())

    # format data received for display
    if player_data != "ERROR: Invalid Search":

        name = player_data["first_name"] + " " + player_data["last_name"]
        team = player_data["team"]["full_name"]
        position = player_data["position"]

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

        if player_data["height_feet"] is None:
            height = "N/A"
        else:
            height = str(player_data["height_feet"]) + " ft " + str(player_data["height_inches"]) + ' in'

        if player_data["weight_pounds"] is None:
            weight = "N/A"
        else:
            weight = str(player_data["weight_pounds"]) + " lbs"

        table_data = [["Name", name], ["Position", position], ["Team", team], ["Height", height], ["Weight", weight]]

        # display data
        print(tabulate(table_data, tablefmt="heavy_grid"))

    else:
        print(f"\n{player_data}\n")


def random_player():

    socket = start_socket()

    # send request to NBA_Player_Microservice.py
    socket.send_string("random")

    # receive response from NBA_Player_Microservice.py
    player = socket.recv_string()

    # display random player name
    print(f"\n{player}\n")
