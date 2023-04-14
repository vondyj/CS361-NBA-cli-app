import pyfiglet
import requests

from InquirerPy import inquirer
from clint.textui import prompt, puts, indent, colored, validators

def main():

    title_text = pyfiglet.figlet_format("NBA CLI APP", font= "slant")
    end_text = pyfiglet.figlet_format("SEE YA!", font= "slant")

    print(title_text)

    main_menu()

    print(end_text)

def main_menu():

    main_menu = inquirer.select(

        message= "What would you like to do?",

        choices= ["View NBA Conferences", 
                  "View Standings by Conference"]

    ).execute()
    
    if main_menu == "View NBA Conferences":
        conferences()

    elif main_menu == "View Standings by Conference":
        conferenceStandings()

def conferences():
    print("\n PLACEHOLDER: conferences \n ")

def conferenceStandings():
    print("\n PLACEHOLDER: standings \n")

if __name__ == "__main__":
    main()
