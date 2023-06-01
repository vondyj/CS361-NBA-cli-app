# A microservice that retrieves information about NBA conferences (divisions or standings) from the following APIs
# then parses that data before returning it.
# API-BASKETBALL - https://rapidapi.com/api-sports/api/api-basketball
# Free NBA - https://rapidapi.com/theapiguy/api/free-nba

import requests
import json
import zmq

# set up socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5554")

# initial startup message
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


def send_standings_request(group):

    print(f"Getting {group} standings data...")

    url = "https://api-basketball.p.rapidapi.com/standings"
    querystring = {"league": "12",
                   "season": "2022-2023",
                   "stage": "NBA",
                   "group": group}
    headers = {
        "content-type": "application/octet-stream",
        "X-RapidAPI-Key": "819d583bd4mshb1f58b42eb6bd5fp143f39jsn6aed4cda8d08",
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return data


def parse_standings_data(data):

    standings = []

    # test = [[x] for x in data['response'][0]]

    # parse data to return to client
    for value in data['response'][0]:           # re-write as list comprehension?
        position = value['position']
        name = value['team']['name']
        wins = value['games']['win']['total']
        losses = value['games']['lose']['total']

        standings.append([position, name, wins, losses])

    return standings


def division_request(request):

    conference = request[:-10]
    print(f"Getting {conference}ern Conference Division data...")

    # set up request
    url = "https://free-nba.p.rapidapi.com/teams"
    headers = {"content-type": "application/octet-stream",
               "X-RapidAPI-Key": "819d583bd4mshb1f58b42eb6bd5fp143f39jsn6aed4cda8d08",
               "X-RapidAPI-Host": "free-nba.p.rapidapi.com"}

    # request info from API
    response = requests.get(url, headers=headers)
    data = response.json()
    divisions = {}

    # parse data received to return to client
    for value in data['data']:
        if value['conference'] == conference:

            if value['division'] not in divisions:
                divisions[value['division']] = value['full_name']
            else:
                divisions[value['division']] = divisions[value['division']] + ", " + (value['full_name'])

    # send response
    print(f"Sending {message} Conference Division data...\n")
    socket.send_json(json.dumps(divisions))


# def send_division_request(group):


# def parse_division_data(data):


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
            error_msg = "ERROR: Please try again."
            socket.send_json(json.dumps(error_msg))
