from random import randint

class Game():

    def __init__(self):
        self.result = ''
        self.player_1 = None
        self.player_2 = None

    def play(self):
        # add check for both players
        if self.player_1.choice == "Rock" and self.player_2.choice == "Rock":
            self.result = "Draw!"
        elif self.player_1.choice == "Rock" and self.player_2.choice == "Paper":
            self.result = self.player_2.name + " wins!"
        elif self.player_1.choice == "Rock" and self.player_2.choice == "Scissors":
            self.result = self.player_1.name + " wins!"
        if self.player_1.choice == "Paper" and self.player_2.choice == "Paper":
            self.result = "Draw!"
        elif self.player_1.choice == "Paper" and self.player_2.choice == "Scissors":
            self.result = self.player_2.name + " wins!"
        elif self.player_1.choice == "Paper" and self.player_2.choice == "Rock":
            self.result = self.player_1.name + " wins!"
        if self.player_1.choice == "Scissors" and self.player_2.choice == "Scissors":
            self.result = "Draw!"
        elif self.player_1.choice == "Scissors" and self.player_2.choice == "Rock":
            self.result = self.player_2.name + " wins!"
        elif self.player_1.choice == "Scissors" and self.player_2.choice == "Paper":
            self.result = self.player_1.name + " wins!"

    def add_player_choice(self, player_number, player):
        setattr(self, f"player_{player_number}", player) 
        # object, propery, value

    def reset_game(self):
        self.player_1 = None
        self.player_2 = None
        self.result = ''
    
    