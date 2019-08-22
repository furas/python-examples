import random

class Player():

    def __init__(self, name):
        self.name = name
        self.score = 0

    def run(self):
        self.score += random.randint(0, 6)

    def __str__(self):
        return "{} (score: {})".format(self.name, self.score)

class Team():
    
    def __init__(self, players):
        self.players = players
        self.current_batsman = 0
        self.current_run = 0
        
    def set_next_batsman(self):
        self.current_batsman += 1
        if self.current_batsman >= len(self.players):
            self.current_batsman = 0
            
    def get_current_batsman(self):
        return self.players[self.current_batsman]
    
    def run(self):
        self.players[self.current_batsman].run()
                
        if self.current_run % 2 != 0:
            self.set_next_batsman()

        self.current_run += 1
        
    def __str__(self):
        return "Player: " + ", ".join(str(p) for p in self.players)
        
    def total_score(self):
        return sum(p.score for p in self.players)
    
team1 = Team( [Player("a"), Player("b"), Player("c")] )
team2 = Team( [Player("x"), Player("y"), Player("z")] )

print('Team1:', team1)
print('Team2:', team2)

for number in range(1, 5):
    print('Round:', number)
    print('Team1 current batsman:', team1.get_current_batsman())
    team1.run()
    print('Team2 current batsman:', team2.get_current_batsman())
    team2.run()

print('Team1:', team1)
print('Team2:', team2)

print('Team1 total score:', team1.total_score())
print('Team2 total score:', team2.total_score())

