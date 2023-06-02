import requests
import json
import zmq

# set up socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5553")
print("\nSocket listening at port 5553...")