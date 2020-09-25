class Game():

    def __init__(self):
        self.result = ''
        self.player_choice = []

    def play(self, player_1, player_2):
        if player_1.choice == "Rock" and player_2.choice == "Rock":
            self.result = "Draw!"
        elif player_1.choice == "Rock" and player_2.choice == "Paper":
            self.result = player_2.name + " wins!"
        elif player_1.choice == "Rock" and player_2.choice == "Scissors":
            self.result = player_1.name + " wins!"
        if player_1.choice == "Paper" and player_2.choice == "Paper":
            self.result = "Draw!"
        elif player_1.choice == "Paper" and player_2.choice == "Scissors":
            self.result = player_2.name + " wins!"
        elif player_1.choice == "Paper" and player_2.choice == "Rock":
            self.result = player_1.name + " wins!"
        if player_1.choice == "Scissors" and player_2.choice == "Scissors":
            self.result = "Draw!"
        elif player_1.choice == "Scissors" and player_2.choice == "Rock":
            self.result = player_2.name + " wins!"
        elif player_1.choice == "Scissors" and player_2.choice == "Paper":
            self.result = player_1.name + " wins!"

    def add_player_choice(self, player_1,player_2):
        self.player_choice.clear()
        self.player_choice.append(player_1)
        self.player_choice.append(player_2)


    def reset_game(self):
        self.player_choice.clear()
        self.result = ''
    