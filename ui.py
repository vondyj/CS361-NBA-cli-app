import pyfiglet
import json
import zmq

from InquirerPy import inquirer
from tabulate import tabulate

from time import sleep
from tqdm import tqdm


def main():

    title_text = pyfiglet.figlet_format("NBA CLI APP", font="digital")
    end_text = pyfiglet.figlet_format("SEE YA!", font="digital")

    print("\n")
    print(title_text)

    # will run until "Exit" is selected
    main_menu()

    print("\n")
    print(end_text)


def main_menu():

    programmer = "Programmed by Jillian Vondy\n"
    intro = "Welcome to my NBA CLI App. To navigate through the app please use the “up” and “down” arrow keys " \
            "to choose a menu option then hit “return” to select it. \n"

    print(programmer)
    print(intro)

    # run the menu until the user chooses to exit
    while True:
        menu = inquirer.select(

            message="Main Menu: What would you like to learn about?",
            choices=["Conferences",
                     "Teams",
                     "Players",
                     "Games",
                     "Resources used",
                     "Exit"]
        ).execute()

        print("\n")

        if menu == "Conferences":
            conferences_menu()
        elif menu == "Teams":
            teams_menu()
        elif menu == "Players":
            players_menu()
        elif menu == "Games":
            games_menu()
        elif menu == "Resources used":
            resources()
        else:
            return


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

    # will run until user selects "Return
    while True:

        menu = inquirer.select(
            message="Conference:",
            choices=["Western",
                     "Eastern",
                     "Return"]
        ).execute()

        if menu == "Western":
            conferences_western()
        elif menu == "Eastern":
            conferences_eastern()
        else:
            return


def conferences_western():

    print("\n")

    # TO DO: revise to work with ZeroMQ socket
    # pass info to "conference division service" (what conference we would like to get the divisions of)
    with open("conference-division-service.txt", "w") as conference_divisions_service_txt:
        conference_divisions_service_txt.write("West")

    # wait for standings service to get info and send it back
    for i in tqdm(range(10), total=10, desc="Getting Western Conference Divisions"):
        sleep(.2)

    # read the data sent from conference division service
    with open("conference-division-service.txt") as conference_divisions_service_txt:
        data = conference_divisions_service_txt.read()

    js_data = json.loads(data)

    # display the standings table
    headings = ["Division", "Teams"]
    print(tabulate([division for division in js_data.items()], headers=headings, tablefmt="psql"))


def conferences_eastern():

    print("\n")

    # TO DO: revise to work with ZeroMQ socket
    # pass info to "conference division service" (what conference we would like to get the divisions of)
    with open("conference-division-service.txt", "w") as conference_divisions_service_txt:
        conference_divisions_service_txt.write("East")

    # wait for standings service to get info and send it back
    for i in tqdm(range(10), total=10, desc="Getting Eastern Conference Divisions"):
        sleep(.2)

    # read the data sent from conference division service
    with open("conference-division-service.txt") as conference_divisions_service_txt:
        data = conference_divisions_service_txt.read()

    js_data = json.loads(data)

    # display the standings table
    headings = ["Division", "Teams"]
    print(tabulate([division for division in js_data.items()], headers=headings, tablefmt="psql"))


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
            western_standings()
        elif menu == "Eastern":
            eastern_standings()
        else:
            return
        

def western_standings():

    print("\n")

    # TO DO: revise to work with ZeroMQ socket
    # pass info to "standings service" (what conference we would like to get the standings for)
    with open("standings-service.txt", "w") as standings_service_txt:
        standings_service_txt.write("west")

    # wait for standings service to get info and send it back
    for i in tqdm(range(10), total=10, desc="Getting Western Conference Standings"):
        sleep(.2)

    # read the data sent from standings service
    with open("standings-service.txt") as standings_service_txt:
        data = standings_service_txt.read()

    js_data = json.loads(data)

    # display the standings table
    headings = ["Position", "Team"]
    print(tabulate([position for position in js_data.items()], headers=headings, tablefmt="psql"))


def eastern_standings():

    print("\n")

    # TO DO: revise to work with ZeroMQ socket
    # pass info to "standings service" (what conference we would like to get the standings for)
    with open("standings-service.txt", "w") as standings_service_txt:
        standings_service_txt.write("east")

    # wait for standings service to get info and send it back
    for i in tqdm(range(10), total=10, desc="Getting Eastern Conference Standings"):
        sleep(.2)

    # read the data sent from standings service
    with open("standings-service.txt") as standings_service_txt:
        data = standings_service_txt.read()

    js_data = json.loads(data)

    # display the standings table
    headings = ["Position", "Team"]
    print(tabulate([position for position in js_data.items()], headers=headings, tablefmt="psql"))


def teams_menu():

    # will run until the user selects "Main menu"
    while True:
        menu = inquirer.select(
            message="Team Options:",
            choices=["Get stats for a specific team",
                     "Get a random team",
                     "Main menu"]

        ).execute()

        if menu == "Get stats for a specific team":
            print("\n PLACEHOLDER: Get stats for a specific team \n")
        elif menu == "Get a random team":
            print("\n PLACEHOLDER: Get a random team \n")
        else:
            print("\n")
            return


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
            return


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
            print("\n PLACEHOLDER: Display games in progress \n")
        elif menu == "View information about a past game":
            print("\n PLACEHOLDER: View information about a past game \n")
        else:
            print("\n")
            return


def resources():
    print("PLACEHOLDER: resources used \n")


if __name__ == "__main__":
    main()
