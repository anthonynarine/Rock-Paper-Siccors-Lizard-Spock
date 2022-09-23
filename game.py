from player import Player
from human import Human
from computer import Computer
import time


class Game:
   
    def __init__(self):
        pass

    def greet_user(self):
        print("*" * 53)
        welcome = f"Welcome to Rock ~ Paper ~ Scissors ~ Lizard ~ Spock!\n"
        welcome += f"\nEach match will be best of the 3 games\n"
        welcome += f"Use the number keys to enter your selection"
        print(welcome)
        print("*" * 53)

    def game_rules(self):
        rules = "\nScissors cuts paper and slices Lizard.\n"
        rules += "Paper smuthers Rock and vanquishes Spock.\n"
        rules += "Rock crushes Lizard and braks Scissors.\n"
        rules += "Lizard eates Paper and Poisons Spock.\n"
        rules += "Spock vaporizes Rock and smashes scissors.\n"
        print (rules)
        print("*" * 53)

    def amount_of_players(slef):
        user = input(f"How many Players? 1 ~ 2 or 3 for a Surprise: ")
        print("*" * 53)
        
        


    # def create_player(self):
    #     self.player_name = Human()
    #     self.computer = Computer()
    #     print(f"You will be going up against {self.computer}")

    








g=Game()
g.greet_user()
g.game_rules()
g.amount_of_players()