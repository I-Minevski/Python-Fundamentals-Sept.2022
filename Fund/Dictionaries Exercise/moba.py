from collections import OrderedDict
import operator

players = {}
while True:
    info = input()
    if info == "Season end":
        break
    elif "->" in info:
        player_info = info.split(" -> ")
        player, position, skill = player_info
        skill = int(skill)
        if player not in players.keys():
            players[player] = {}
        if position not in players[player].keys():
            players[player][position] = skill
        if players[player][position] < skill:
            players[player][position] = skill
    else:
        duel = info.split(" vs ")
        pl1, pl2 = duel
        if pl1 in players.keys() and pl2 in players.keys():
            have_common = any(pos in players[pl1].keys() for pos in players[pl2].keys())
            if have_common == True:
                score1 = sum(players[pl1].values())
                score2 = sum(players[pl2].values())
                if score1 < score2:
                    del players[pl1]
                elif score1 > score2:
                    del players[pl2]

sorted_names = {}
for key in players.keys():
    sorted_names[key] = sum(players[key].values())
sorted_keys = sorted(sorted_names.keys())
sorted_names = {key:sorted_names[key] for key in sorted_keys} 
sorted_names = dict(sorted(sorted_names.items(), key=lambda x:x[1], reverse=True))

for (key, value) in sorted_names.items():
    print(f"{key}: {value} skill")
    sorted_keys_player = sorted(players[key].keys())
    sorted_positions = {i: players[key][i] for i in sorted_keys_player}
    sorted_positions = dict(sorted(sorted_positions.items(), key=lambda x: x[1], reverse=True))
    for (k, v) in sorted_positions.items():
        print(f"- {k} <::> {v}")
