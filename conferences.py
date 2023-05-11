import json

from InquirerPy import inquirer
from tqdm import tqdm
from time import sleep
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
    for _ in tqdm(range(10), total=10, desc="Getting Western Conference Divisions"):
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