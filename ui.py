import pyfiglet

from InquirerPy import inquirer

from conferences import conferences_menu
from teams import teams_menu
from players import players_menu
from games import games_menu
from resources import resources


def main():

    intro_message()
    main_menu()
    outro_message()


def main_menu():

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

        match menu:
            case "Conferences":             # implemented
                conferences_menu()
            case "Teams":                   # TO DO
                teams_menu()
            case "Players":                 # implemented
                players_menu()
            case "Games":                   # in-progress
                games_menu()
            case "Resources used":          # in-progress
                print("test")
                resources()
            case "Exit":
                return
            case _:
                return


def intro_message():

    title_text = pyfiglet.figlet_format("NBA CLI APP", font="3-d")
    intro_text = f"\nWelcome to my NBA CLI App. To navigate through the app please use the “up” and “down” arrow keys" \
                 " to choose a menu option then hit “return” to select it.\n"

    print(f"\n{title_text}\n{intro_text}")


def outro_message():

    end_text = pyfiglet.figlet_format("SEE YA!", font="3-d")
    print(f"\n{end_text}")


if __name__ == "__main__":
    main()
