import pyfiglet

from InquirerPy import inquirer

from conferences import conferences_menu
from teams import teams_menu
from players import players_menu
from games import games_menu
from resources import resources


def main():

    # set up intro and exit text
    title_text = pyfiglet.figlet_format("NBA CLI APP", font="3-d")
    end_text = pyfiglet.figlet_format("SEE YA!", font="3-d")

    print(f"\n{title_text}")

    # will run until "Exit" is selected
    main_menu()

    print(f"\n{end_text}\n")


def main_menu():

    intro = "Welcome to my NBA CLI App. To navigate through the app please use the “up” and “down” arrow keys " \
            "to choose a menu option then hit “return” to select it. \n"

    print(intro)

    # display the menu until the user chooses "Exit"
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

        if menu == "Conferences":           # implemented
            conferences_menu()
        elif menu == "Teams":               # TO DO
            teams_menu()
        elif menu == "Players":             # in progress
            players_menu()
        elif menu == "Games":               # TO DO
            games_menu()
        elif menu == "Resources used":      # TO DO
            resources()
        else:
            return


if __name__ == "__main__":
    main()
