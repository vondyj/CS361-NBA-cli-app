Resources Used

  4/13/23
  https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/

  4/13/23
  https://rapidapi.com/blog/free-nba-api-with-python-php-ruby-and-javascript/

  4/13/23
  https://www.w3schools.com/python/pandas/pandas_dataframes.asp

  4/13/23
  https://pypi.org/project/clint/

  4/13/23
  https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/?ref=lbp#

  4/13/23
  https://github.com/kennethreitz-archive/clint/blob/master/examples/prompt.py

APIs

  4/13/23
  https://rapidapi.com/theapiguy/api/free-nba

  4/23/23
  https://app.balldontlie.io/

  4/13/23 
  https://rapidapi.com/api-sports/api/api-basketball

## NBA Player Microservice Communication Contract:
This is the communication contract for use of NBA_Player_Microservice.py. Example calls are also available in the file nba_tester.py.
### REQUEST:
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
### RECEIVE:
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
### UML Sequence Diagram:
![image](https://user-images.githubusercontent.com/129910818/236729668-0805d0d5-86ac-4f48-97ff-e31d8b09e496.png)
