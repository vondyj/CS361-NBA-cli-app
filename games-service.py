import zmq
import requests

from datetime import datetime

# set up socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:9999")
print("\nSocket listening at port 9999...")


def games_in_progress_request():

    data = send_games_in_progress_request()
    games = parse_games_in_progress_data(data)

    print(f"Sending games in progress...\n")
    socket.send_json(games)


def send_games_in_progress_request():

    today = get_today()                # test date with confirmed games: '2023-03-01'
    print(f"Finding games on {today}...")

    payload = {'start_date': today,
               'end_date': today}
    request = requests.get("https://www.balldontlie.io/api/v1/games", params=payload)
    return request.json()


def parse_games_in_progress_data(data):

    games = []

    match data['data']:
        case []:
            games = "None"
        case _:
            for value in data["data"]:
                home_team = value["home_team"]["full_name"]
                home_score = value["home_team_score"]
                visitor_team = value["visitor_team"]["full_name"]
                visitor_score = value["visitor_team_score"]
                period = value["period"]

                games.append([home_team, visitor_team, home_score, visitor_score, period])

    return games


def get_today():

    return datetime.today().strftime('%Y-%m-%d')


while True:

    # receive request from client
    message = socket.recv_string()
    print(f"\nReceived message: {message}")

    match message:
        case "in progress":
            games_in_progress_request()
        case _:
            print("ERROR")
