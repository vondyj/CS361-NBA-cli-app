from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll 

import pandas as pd

player_dict = players.get_players()
team_dict = teams.get_teams()

print(player_dict)
print(team_dict)



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