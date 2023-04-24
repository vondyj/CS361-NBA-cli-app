import pyfiglet
import requests

from InquirerPy import inquirer
from clint.textui import prompt, puts, indent, colored, validators


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

    intro = "Welcome to my NBA CLI App. To navigate through the app please use the “up” and “down” arrow keys \n" \
            "to choose a menu option then hit “return” to select it. \n"

    print(intro)

    # run the menu until the user chooses to exit
    while True:
        menu = inquirer.select(

            message="What would you like to learn about?",
            choices=["Conferences",
                     "Teams",
                     "Players",
                     "Games",
                     "Resources used",
                     "Exit"]

        ).execute()

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
            conferences_divisions()
        elif menu == "View standings by conference":
            conference_standings()
        else:
            print("\n")
            return


def conferences_divisions():

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
    print("placeholder")


def conferences_eastern():
    print("placeholder")


def conference_standings():

    # will run until user selects "Return
    while True:

        menu = inquirer.select(
            message="Conference:",
            choices=["Western",
                     "Eastern",
                     "Return"]
        ).execute()

        if menu == "Western":
            print("\n PLACEHOLDER: Western \n")
        elif menu == "Eastern":
            print("\n PLACEHOLDER: Eastern \n")
        else:
            return


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
            print("\n PLACEHOLDER: Get stats for a specific player \n")
        elif menu == "Get a random player":
            print("\n PLACEHOLDER: Get a random player \n")
        else:
            print("\n")
            return


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
    print("\n PLACEHOLDER: resources used \n")


if __name__ == "__main__":
    main()
