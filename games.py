
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
            print("\n PLACEHOLDER: Display games in progress \n")
        elif menu == "View information about a past game":
            print("\n PLACEHOLDER: View information about a past game \n")
        else:
            print("\n")
            return