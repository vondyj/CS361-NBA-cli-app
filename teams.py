from InquirerPy import inquirer


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
            break
