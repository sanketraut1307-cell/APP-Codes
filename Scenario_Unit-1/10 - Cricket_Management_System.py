# Scenario - 10
class Player:
    def __init__(self, name, jersey, runs):
        self.name = name
        self.jersey = jersey
        self.runs = runs

    def category(self):
        if self.runs >= 500:
            return "Excellent"
        elif self.runs >= 250:
            return "Good"
        else:
            return "Average"


class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_players(self):
        print("Cricket Team Players")
        print("---------------------")

        for p in self.players:
            print("Name:", p.name)
            print("Jersey Number:", p.jersey)
            print("Runs:", p.runs)
            print("Category:", p.category())
            print("---------------------")


# Create team
team = Team()

# Add players
team.add_player(Player("Virat Kohli", 18, 750))
team.add_player(Player("Rohit Sharma", 45, 400))
team.add_player(Player("KL Rahul", 1, 180))

# Display all players
team.display_players()

#Output - 
#Cricket Team Players
#---------------------
#Name: Virat Kohli
#Jersey Number: 18
#Runs: 750
#Category: Excellent
#---------------------
#Name: Rohit Sharma
#Jersey Number: 45
#Runs: 400
#Category: Good
#---------------------
#Name: KL Rahul
#Jersey Number: 1
#Runs: 180
#Category: Average
#---------------------
