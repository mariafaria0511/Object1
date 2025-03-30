
class Team:
    def __init__(self, name):
        self.name = name

class Player:
    def __init__(self, playername, playerposition):
        self.playername = playername
        self.playerposition = playerposition

p1 = Player("Joe Montana", "Quarterback")
p2 = Player("Barry Sanders", "Running Back")
p3 = Player("Jerry Rice", "Wide Receiver")
p4 = Player("Graham Gano", "Kicker")

team_name = Team("NFLTeam")

playerList = [p1,p2,p3,p4]

print(team_name.name)
print(playerList[0].playername, playerList[0].playerposition)
print(playerList[1].playername, playerList[1].playerposition)
print(playerList[2].playername, playerList[2].playerposition)
print(playerList[3].playername, playerList[3].playerposition)
