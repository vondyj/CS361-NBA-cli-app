import json
import zmq

from InquirerPy import inquirer
from tabulate import tabulate


def conferences_menu():
    #  will be displayed until the user selects "Main menu"
    while True:
        menu = inquirer.select(
            message='Conference Options:',
            choices=["View conferences and divisions",
                     "View standings by conference (regular season)",
                     "Main menu"]
        ).execute()

        match menu:
            case "View conferences and divisions":
                conference_divisions_menu()
            case "View standings by conference (regular season)":
                conference_standings_menu()
            case _:
                print("\n")
                return


def conference_divisions_menu():
    # will be displayed until user selects "Return"
    while True:
        menu = inquirer.select(
            message="Conference:",
            choices=["Western",
                     "Eastern",
                     "Return"]
        ).execute()

        match menu:
            case "Western":
                conferences("West Divisions")
            case "Eastern":
                conferences("East Divisions")
            case _:
                return


def conference_standings_menu():
    # will run until user selects "Return"
    while True:

        menu = inquirer.select(
            message="Conference:",
            choices=["Western",
                     "Eastern",
                     "Return"]
        ).execute()

        match menu:
            case "Western":
                standings("West Standings")
            case "Eastern":
                standings("East Standings")
            case _:
                return
        

def start_socket():
    # set up communication with conference-service.py
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5554")

    # return the socket to the method that called it for communication purposes
    return socket


def conferences(conference):
    # send request to conference-service.py
    socket = start_socket()
    socket.send_string(conference)

    # receive response
    js_data = json.loads(socket.recv_json())

    # display table title
    print(f"\n{conference[:-10]}ern Conference Divisions")

    # display the conference table
    headings = ["Division", "Teams"]
    print(tabulate((item for item in js_data.items()), headings, tablefmt="heavy_grid", maxcolwidths=[None, 40]))


def standings(conference):
    # send request to conference-service.py
    socket = start_socket()
    socket.send_string(conference)

    # receive response
    js_data = json.loads(socket.recv_json())

    # display table title
    print(f"\n{conference[:-10]}ern Conference Standings")

    # display the standings table
    headings = ["Position", "Team", "Wins", "Losses"]
    print(tabulate((item for item in js_data), headings, tablefmt="heavy_grid"))
