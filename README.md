## NBA Player Microservice Communication Contract
This is the communication contract for use of NBA_Player_Microservice.py. Example calls are also available in the file nba_tester.py.
### REQUEST
To request from this microservice, use ZeroMQ to connect REQ socket to localhost:5555 and send either “random” for a random player name, or the players name to search for. 
Example request:
```
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
# send string with player name OR
socket.send_string(player)
# send string “random” for random player
socket.send_string("random")
```
### RECEIVE
Data is received from this microservice through the same ZeroMQ REQ socket at localhost:5555. Data will be returned as either a string or JSON.
Searching for a player by name returns a JSON of the player data, which can be received like so:
```
player_data = json.loads(socket.recv())
```
If there is no player with the name searched for, microservice will return a string stating the error.
Searching for a random player name returns a string which can be received like so:
```
rand_player = socket.recv().decode()
```
### UML Sequence Diagram
![image](https://user-images.githubusercontent.com/129910818/236729668-0805d0d5-86ac-4f48-97ff-e31d8b09e496.png)

## Resources Used

### Free Code Camp
[Python Requests – How to Interact with Web Services using Python ](https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/)
### Free NBA API
[How to Use The Free NBA API with Python, PHP, Ruby and JavaScript](https://rapidapi.com/blog/free-nba-api-with-python-php-ruby-and-javascript/)
### Geeks for Geeks
[Python | ASCII art using pyfiglet module](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/?ref=lbp#)
### InquirerPy
[Read the docs](https://inquirerpy.readthedocs.io/en/latest/)
### ZeroMQ 
[Get started](https://zeromq.org/get-started/)
  
## APIs

### [API-BASKETBALL](https://rapidapi.com/api-sports/api/api-basketball)
### [Free NBA](https://rapidapi.com/theapiguy/api/free-nba)
### [Ball Don't Lie](https://app.balldontlie.io/)
