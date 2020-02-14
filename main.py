import team, player
import copy
import operator
import time
import datetime

def get_player_list(file_name):
    with open(file_name) as f:
        player_strings = f.readlines()

    players = []
    for player_string in player_strings[1:]:
        players.append(player.Player.fromCSV(player_string))
    return players

def add_player(team, players, positions, index):
    if index >= len(positions):
        if team._salary <= 50000:
            sorted_teams = sorted(VALID_TEAMS, reverse=True, key=operator.attrgetter('_points'))
            if len(VALID_TEAMS) < 10:
                VALID_TEAMS.append(copy.deepcopy(team))
            elif team._points < sorted_teams[-1]:
                sorted_teams[-1] = copy.copy(team)
        return
    for player in players:
        pos = positions[index]
        if index == 0:
            ts = time.time()
            print datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'), player._id
        if player.plays_position(pos) and not team.player_in_team(player) and player._points > 8:
            team.add_player(player, pos)
            if team._salary > 50000:
                team.remove_player(player, pos)
                return 
            add_player(team, players, positions, index +1)
            team.remove_player(player, pos)

VALID_TEAMS = []

positions = ["C","C","W","W","D","G"]

team = team.Team(positions)
players = get_player_list("NHL.csv")
add_player(team, players, positions, 0)

sorted_teams = sorted(VALID_TEAMS, key=operator.attrgetter('_points'))

print len(VALID_TEAMS)

for team in sorted_teams[:3]:
    print team

# c
# c
# w
# w
# w
# D
# D
# G
# UTIL
# 50k