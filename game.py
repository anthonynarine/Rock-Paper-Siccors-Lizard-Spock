from telnetlib import GA
from player import Player
from human import Human
from computer import Computer
import time
import random


class Game:
   
    def __init__(self):
        self.planyer_one = None
        self.player_two = None
        self.computer = None
        self.amount_of_players = 0
        self.computer_socre = 0
        self.player_one_score = 0
        self.player_two_socre = 0
        self.tie = 0

 

    # def greet_user(self):
    #     print("-------------------------------------------------------------")
    #     welcome = f"Welcome to Rock ~ Paper ~ Scissors ~ Lizard ~ Spock!\n"
    #     welcome += f"\nEach match will be best of the 3 round\n"
    #     welcome += f"Use the number keys to enter your selection"
    #     print(welcome)
    #     print("-------------------------------------------------------------")


    # def game_rules(self):

        # print("------------------------------------------------------------")
        # print("The game rules are as follows:")
        # rules = "\nScissors cuts paper and slices Lizard.\n"
        # rules += "Paper smuthers Rock and vanquishes Spock.\n"
        # rules += "Rock crushes Lizard and breaks Scissors.\n"
        # rules += "Lizard eats Paper and Poisons Spock.\n"
        # rules += "Spock vaporizes Rock and smashes scissors.\n"
        # print (rules)
        # print("------------------------------------------------------------")


    def creat_player(self):
        number_of_player = int(input(("How many player will we have today?\n1 ~ 2 or 3 for a surprise  ")))
        if number_of_player == 1:
            name = input ("Enter your name player: ")
            self.player_one = Human(name)
            self.computer = Computer()


    # def round1(self):
    #     self.player_one.choose_gesture()
    #     self.




    # def ai_turn(self):
    #     self.computer = Computer()
    #     return self.computer.gesture

g = Game()
g.creat_player()
print(g.player_one.name)
print(g.computer.name)










# g=Game()

# g.user_turn()
# g.ai_turn()
# print(g.computer.gesture)




    
    # def create_players(self):
    #     player_name = input ("Tell me your name Human: ")
    #     self.human_player = Human()

        
        


    # def create_player(self):
    #     self.player_name = Human()
    #     self.computer = Computer()
    #     print(f"You will be going up against {self.computer}")

    








# g = Game()
# g.game_rules()
# g.participants()


