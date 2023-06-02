import zmq

from InquirerPy import inquirer
from tabulate import tabulate
from datetime import datetime


def games_menu():

    # will run until the user selects "Main menu"
    while True:
        menu = inquirer.select(
            message="Game Options:",
            choices=["Display games in progress",
                     "View information about a past game",
                     "Main menu"]

        ).execute()

        match menu:
            case "Display games in progress":
                games_in_progress("in progress")
            case "View information about a past game":
                print("\n PLACEHOLDER: View information about a past game \n")
            case _:
                print("\n")
                return


def start_socket():

    # set up communication with conference-service.py
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:9999")

    # return the socket to the method that called it for communication purposes
    return socket


def games_in_progress(message):

    socket = start_socket()
    socket.send_string(message)

    data = socket.recv_json()

    match data:
        case "None":
            print(f"\nSorry, there are no NBA games today.\n")
        case _:
            print(f"\n NBA Games on {datetime.today().strftime('%Y-%m-%d')}")

            # display the games in progress table
            headings = ["Home Team", "Visitor Team", "Home Score", "Visitor Score", "Period"]
            print(tabulate((item for item in data), headings, tablefmt="heavy_grid"))
