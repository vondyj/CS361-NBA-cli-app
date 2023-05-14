import requests
import json
import zmq

# set up socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5554")

# initial startup message
print("\nSocket listening at port 5554...")

while True:

    # receive request from client
    message = socket.recv_string()

    # handle valid division requests
    if message == "West Divisions" or message == "East Divisions":

        conference = message[:-10]
        print(f"\nRequesting {conference}ern Conference Division data...")

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

    # handle valid standings requests
    elif message == "West Standings" or message == "East Standings":

        conference = message[:-10]

        if conference == "West":
            group = "Western Conference"
        elif conference == "East":
            group = "Eastern Conference"
        else:
            group = ""

        if group != "":

            print(f"\nRequesting {group} standings data...")

            # set up request
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

            # request info from API
            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()

            standings = []

            # parse data to return to client
            for value in data['response'][0]:

                position, name = value['position'], value['team']['name']
                wins, losses = value['games']['win']['total'], value['games']['lose']['total']

                standings.append([position, name, wins, losses])

            print(f"Sending {group} standings data...\n")

            socket.send_json(json.dumps(standings))

    # handle any other requests (errors)
    else:
        error_msg = "ERROR: Please try again."
        socket.send_json(json.dumps(error_msg))
