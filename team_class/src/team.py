class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0    

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_to_check):
        # for player in self.players:
        #     if player == player_to_check:
        #         return True
        # else:
        #      return False   
#  or
        if player_to_check in self.players:
            return True
        else:
            return False

    def play_game(self, game_won):
        # if game_won == True:
        #     self.points = self.points + 3
#  or 
        if game_won:
            self.points += 3