class Game():
    def play(self, player_1, player_2):
        if player_1.choice == "Rock" and player_2.choice == "Rock":
            return "Draw!"
        elif player_1.choice == "Rock" and player_2.choice == "Paper":
            return player_2.name + " wins!"
        elif player_1.choice == "Rock" and player_2.choice == "Scissors":
            return player_1.name + " wins!"
        if player_1.choice == "Paper" and player_2.choice == "Paper":
            return "Draw!"
        elif player_1.choice == "Paper" and player_2.choice == "Scissors":
            return player_2.name + " wins!"
        elif player_1.choice == "Paper" and player_2.choice == "Rock":
            return player_1.name + " wins!"
        if player_1.choice == "Scissors" and player_2.choice == "Scissors":
            return "Draw!"
        elif player_1.choice == "Scissors" and player_2.choice == "Rock":
            return player_2.name + " wins!"
        elif player_1.choice == "Scissors" and player_2.choice == "Paper":
            return player_1.name + " wins!"

    
