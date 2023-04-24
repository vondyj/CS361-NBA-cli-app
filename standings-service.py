import requests
import json
from time import sleep

url = "https://api-basketball.p.rapidapi.com/standings"

while True:

    sleep(1)

    with open("standings-service.txt") as standings_service_txt:
        conference = standings_service_txt.read()

    if conference == "west":
        group = "Western Conference"
    elif conference == "east":
        group = "Eastern Conference"
    else:
        group = ""

    if group !="":

        querystring = {"league":"12",
                    "season":"2022-2023",
                    "stage":"NBA",
                    "group": group}

        headers = {
            "content-type": "application/octet-stream",
            "X-RapidAPI-Key": "819d583bd4mshb1f58b42eb6bd5fp143f39jsn6aed4cda8d08",
            "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
        }

        print(f"Getting {group} standings data...")

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        standings = {}

        for value in data['response'][0]:
            standings.update({value['position']: value['team']['name']})
 
        print(f"Sending {group} standings data...\n")

        with open("standings-service.txt", "w") as standings_service_txt:
            standings_service_txt.write(json.dumps(standings))
