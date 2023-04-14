from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll 

import pandas 
import requests

player_dict = players.get_players()
team_dict = teams.get_teams()


# player example
bron = [player for player in player_dict if player['full_name'] == 'LeBron James'] [0]
bron_id = bron['id']

gamelog_bron = playergamelog.PlayerGameLog(player_id=str(bron_id), season='2018')
df_bron_games_2018 = gamelog_bron.get_data_frames()

game_log_bron_all = playergamelog.PlayerGameLog(player_id='2544' ,season=SeasonAll.all)
df_bron_games_all = game_log_bron_all.get_data_frames()

print(bron)
print(bron_id)
print(df_bron_games_2018)
print(df_bron_games_all)

# team example
GSW = [team for team in team_dict if team['full_name'] =='Golden State Warriors'][0]
GSW_id = GSW['id']

print(GSW)
print(GSW_id)

# conference example
url = "https://free-nba.p.rapidapi.com/teams"

querystring = {
    "conference":"East"
    }

headers = {
	"X-RapidAPI-Key": "819d583bd4mshb1f58b42eb6bd5fp143f39jsn6aed4cda8d08",
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

eastern_conference = requests.request("GET", url, headers=headers, params=querystring)

for team in eastern_conference:
    print(team[0])


# western_conference = [team for team in team_dict if team['conference'] == 'Western']
