import pyfiglet

from InquirerPy import inquirer

from conferences import conferences_menu
from teams import teams_menu
from players import players_menu
from games import games_menu
from resources import resources


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

    intro = "Welcome to my NBA CLI App. To navigate through the app please use the “up” and “down” arrow keys " \
            "to choose a menu option then hit “return” to select it. \n"

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


if __name__ == "__main__":
    main()
