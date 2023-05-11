import zmq
import json

#This function will be used to request player data by searching by name:
def player_search():
    context = zmq.Context()
    player = input("Enter player name:")
    print("Connecting to NBA player server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    print(f"Sending request...")
    socket.send_string(player)
    # receive serialized data (JSON) from microservice
    player_data = json.loads(socket.recv())
    print(player_data)

#This function will be used to request a random player name:
def random_player():
    context = zmq.Context()
    print("Connecting to NBA player server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    print(f"Sending request...")
    socket.send_string("random")
    # receive serialized data (JSON) from microservice
    rand_player = socket.recv().decode()
    print(rand_player)

random_player()
player_search()

