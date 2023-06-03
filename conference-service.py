# A microservice that retrieves information about NBA conferences (divisions or standings) from the following APIs
# then parses that data before returning it.
# API-BASKETBALL - https://rapidapi.com/api-sports/api/api-basketball
# Free NBA - https://rapidapi.com/theapiguy/api/free-nba

import requests
import json
import zmq

from config import api_basketball_key, free_nba_key

from datetime import datetime

# set up socket on start 
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5554")
print("\nSocket listening at port 5554...")


def standings_request(request):
    match request[:-10]:
        case "West":
            group = "Western Conference"
        case "East":
            group = "Eastern Conference"
        case _:
            group = None

    if group:
        data = send_standings_request(group)
        standings = parse_standings_data(data)

        print(f"Sending {group} standings data...\n")
        socket.send_json(json.dumps(standings))
    else:
        error_message()


def send_standings_request(group):
    print(f"Getting {group} standings data...")

    season = get_season()
    url = "https://api-basketball.p.rapidapi.com/standings"
    querystring = {"league": "12",
                   "season": season,
                   "stage": "NBA",
                   "group": group}
    headers = {
        "content-type": "application/octet-stream",
        "X-RapidAPI-Key": api_basketball_key,
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return data


def parse_standings_data(data):
    standings = []

    for value in data['response'][0]:
        standings.append([value['position'], 
                          value['team']['name'], 
                          value['games']['win']['total'], 
                          value['games']['lose']['total']])

    return standings


def division_request(request):
    conference = request[:-10]
    data = send_division_request(conference)
    divisions = parse_division_data(data, conference)

    # send response
    print(f"Sending {message} Conference Division data...\n")
    socket.send_json(json.dumps(divisions))


def send_division_request(conference):
    print(f"Getting {conference}ern Conference Division data...")

    # set up request
    url = "https://free-nba.p.rapidapi.com/teams"
    headers = {"content-type": "application/octet-stream",
               "X-RapidAPI-Key": free_nba_key,
               "X-RapidAPI-Host": "free-nba.p.rapidapi.com"}

    # request info from API
    response = requests.get(url, headers=headers)
    data = response.json()
    return data


def parse_division_data(data, conference):
    divisions = {}

    # parse data received to return to client
    for value in data['data']:
        if value['conference'] == conference:

            if value['division'] not in divisions:
                divisions[value['division']] = value['full_name']
            else:
                divisions[value['division']] = divisions[value['division']] + ", " + (value['full_name'])

    return divisions


def error_message():
    error_msg = "ERROR: Please try again."
    socket.send_json(json.dumps(error_msg))


def get_season():
    current_year = datetime.today().year
    season = f"{str(current_year - 1)}-{str(current_year)}"
    return season


while True:
    # receive request from client
    message = socket.recv_string()
    print(f"\nReceived message: {message}")

    match message[5:]:
        case "Standings":
            standings_request(message)
        case "Divisions":
            division_request(message)
        case _:
            error_message()
