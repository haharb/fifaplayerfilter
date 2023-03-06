import csv
filePlayers = open('players_fifa23.csv', encoding = 'utf8')
fileTeams = open('players_fifa23.csv', encoding = 'utf8')
csvreader = csv.reader(filePlayers)
playersHeader = []
teamsHeader = []
playersHeader = next(csvreader)

players = []
teamRows = []
for row in csvreader:
    players.append(row)
csvreader = csv.reader(fileTeams)
teamsHeader = next(csvreader)
for row in csvreader:
    teamRows.append(row)
#for player in playerRows:
#    if player[playersHeader.index("Nationality")] == "Germany" and ("ST" in player[playersHeader.index("Position")]
print(players[0][players])



filePlayers.close()
filePlayers.close()