import csv
filePlayers = open('players_fifa23.csv', encoding = 'utf8')
fileTeams = open('teams_fifa23.csv', encoding = 'utf8')
csvreaderp = csv.reader(filePlayers)
csvreadert = csv.reader(fileTeams)
playersHeader = []
teamsHeader = []
playersHeader = next(csvreaderp)
playersHeader.append("League")
players = []
teams = []
for rowp in csvreaderp:
    players.append(rowp)
csvreader = csv.reader(fileTeams)
teamsHeader = next(csvreadert)
for rowt in csvreadert:
    teams.append(rowt)
teams[teamsHeader.index("Name")]
for team in teams:
    for player in players:
        league = player[playersHeader.index("Club")]
        player.append()
found = []
print(playersHeader)
for player in players:
    if player[playersHeader.index("Nationality")] == "Spain" and ("ST" in player[playersHeader.index("Positions")]):
        teamName = player[playersHeader.index("Club")]
        playerName = player[playersHeader.index("FullName")]
        position = player[playersHeader.index("Positions")]
        result = [playerName, teamName, position]
        found.append(result)

print(found)
#print(playersHeader)



filePlayers.close()
filePlayers.close()