# retrieve information about NBA players from Free NBA API based on user input or random
# data retrieved from https://rapidapi.com/theapiguy/api/free-nba/
import zmq
import requests
import random
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
while True:
    print("\nSocket listening at port 5555...")
    message = socket.recv().decode()
    print(f"Received message: {message}")
    headers = {
        "X-RapidAPI-Key": "83e4b71683mshdcdde29696da6bep10e6a6jsn9baf1733ca0c",
        "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
    }
    if message != "random":
        url = f"https://free-nba.p.rapidapi.com/players/?search={message}"
        response = requests.get(url, headers=headers)
        data = response.json()
        if data['meta']['total_count'] == 0:
            response = "ERROR: Invalid Search"
            print(response)
            socket.send_string(json.dumps(response))
        else:
            print("Player found, returning player data")
            socket.send_string(json.dumps(data['data'][0]))
    else:
        id = random.randint(0, 3093)
        url = f"https://free-nba.p.rapidapi.com/players/{id}"
        response = requests.get(url, headers=headers)
        data = response.json()
        player_data = data['first_name'] + " " + data['last_name']
        print("Returning random player name")
        socket.send_string(player_data)






