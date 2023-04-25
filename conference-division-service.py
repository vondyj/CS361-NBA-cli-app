import requests
import json
from time import sleep

url = "https://free-nba.p.rapidapi.com/teams"
conference = ""

while True:

    sleep(1)

    with open("conference-division-service.txt") as conference_division_txt:
        conference = conference_division_txt.read()

    page = 0
    querystring = {"page":str(page)}

    if conference == 'West' or conference == 'East':
    
        headers = {
	        "content-type": "application/octet-stream",
	        "X-RapidAPI-Key": "819d583bd4mshb1f58b42eb6bd5fp143f39jsn6aed4cda8d08",
	        "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
        }

        print(f"Getting {conference}ern Conference Division data...")

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        divisions = {}

        for value in data['data']:
            if value['conference'] == conference and value['division'] not in divisions:
                divisions[value['division']] = [value['full_name']]
            elif value['conference'] == conference and value['division'] in divisions:
                divisions[value['division']].append(value['full_name'])

        print(f"Sending {conference}ern Conference Division data...\n")

        with open("conference-division-service.txt", "w") as conference_division_txt:
            conference_division_txt.write(json.dumps(divisions))
