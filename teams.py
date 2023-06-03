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

        match menu:
            case "Get stats for a specific team":
                print("\n PLACEHOLDER: Get stats for a specific team \n")
            case "Get a random team":
                print("\n PLACEHOLDER: Get a random team \n")
            case _:
                print("\n")
                return
