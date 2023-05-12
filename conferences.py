import json
import zmq

from InquirerPy import inquirer
from tabulate import tabulate


def conferences_menu():
    # will run until the user selects "Main menu"
    while True:
        menu = inquirer.select(
            message='Conference Options:',
            choices=["View conferences and divisions",
                     "View standings by conference",
                     "Main menu"]
        ).execute()

        if menu == "View conferences and divisions":
            conferences_divisions_menu()
        elif menu == "View standings by conference":
            conference_standings_menu()
        else:
            print("\n")
            return


def conferences_divisions_menu():
    # will run until user selects "Return"
    while True:

        menu = inquirer.select(
            message="Conference:",
            choices=["Western",
                     "Eastern",
                     "Return"]
        ).execute()

        if menu == "Western":
            conferences("West Divisions")
        elif menu == "Eastern":
            conferences("East Divisions")
        else:
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

        if menu == "Western":
            standings("West Standings")
        elif menu == "Eastern":
            standings("East Standings")
        else:
            return
        

def start_socket():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5554")

    return socket


def conferences(conference):

    # send request to conference-service.py
    socket = start_socket()
    socket.send_string(conference)

    # receive response from conference-service.py
    js_data = json.loads(socket.recv_json())

    # display table title
    print(f"\n{conference[:-10]}ern Conference Divisions")

    # display the conference table
    headings = ["Division", "Teams"]
    print(tabulate((item for item in js_data.items()), headings, maxcolwidths=[None, 40], tablefmt="heavy_grid"))


def standings(conference):

    # send request to conference-service.py
    socket = start_socket()
    socket.send_string(conference)

    # receive response from conference-service.py
    js_data = json.loads(socket.recv_json())

    # display table title
    print(f"\n{conference[:-10]}ern Conference Standings")

    # display the standings table
    headings = ["Position", "Team", "Wins", "Losses"]
    print(tabulate((item for item in js_data), headings, tablefmt="heavy_grid"))
