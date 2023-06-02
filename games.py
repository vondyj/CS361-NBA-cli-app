import json
import zmq

from InquirerPy import inquirer


def games_menu():

    # will run until the user selects "Main menu"
    while True:
        menu = inquirer.select(
            message="Game Options:",
            choices=["Display games in progress",
                     "View information about a past game",
                     "Main menu"]

        ).execute()

        if menu == "Display games in progress":
            games_in_progress()
        elif menu == "View information about a past game":
            print("\n PLACEHOLDER: View information about a past game \n")
        else:
            print("\n")
            return


def games_in_progress():

    socket = start_socket()
    socket.send_string("in progress")

    # receive response
    js_data = json.loads(socket.recv_json())

    print(json.dumps(js_data, indent=4))


def start_socket():

    # set up communication with conference-service.py
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5553")

    # return the socket to the method that called it for communication purposes
    return socket
