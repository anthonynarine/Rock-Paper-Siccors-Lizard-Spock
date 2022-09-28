

from human import Human
from computer import Computer
import random
import time

class Game:
   
    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.computer = None

        
    def greet_user(self):
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        welcome = f"Welcome to Rock ~ Paper ~ Scissors ~ Lizard ~ Spock!\n"
        welcome += f"\nEach match will be best of the 3 rounds\n"
        welcome += f"Use the number keys to enter your selection"
        print(welcome)
        print("----------------------------------------------------------")                                                       
        print("----------------------------------------------------------")


    def game_rules(self):

        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("The game rules are as follows:")
        rules = "\nScissors cuts paper and slices Lizard.\n"
        rules += "Paper smuthers Rock and vanquishes Spock.\n"
        rules += "Rock crushes Lizard and breaks Scissors.\n"
        rules += "Lizard eats Paper and Poisons Spock.\n"
        rules += "Spock vaporizes Rock and smashes scissors.\n"
        print (rules)
        print("-----------------------------------------------------------")
        print("-----------------------------------------------------------")


    def n_of_players(self):
        ...

    def creat_player(self):
        # number_of_player = int(input(("How many players will we have today?\n1 ~ 2 or 3 for a surprise  ")))
        # if number_of_player == 1:
            print("\n" * 100)
            name = input ("Enter your name player: ")
            if not name:
                raise ValueError ("Missing name")
            self.player_one = Human(name)
            self.computer = Computer()


    def battle(self):
            self.player_one.choose_gesture()
            self.computer.choose_gesture()

            if self.player_one.current_gesture == self.computer.current_gesture:
                print ("Its a tie, next round")

            elif self.player_one.current_gesture == 1 and self.computer.current_gesture == 3 or self.computer.choose_gesture == 4:
                print (f"{self.player_one.name} has won this round.")
                self.player_one.score += 1

            elif self.player_one.current_gesture == 2 and self.computer.current_gesture == 1 or self.computer.choose_gesture == 5:
                print (f"{self.player_one.name} has won this round.")
                self.player_one.score += 1

            elif self.player_one.current_gesture == 3 and self.computer.current_gesture == 2 or self.computer.choose_gesture == 4:
                print (f"{self.player_one.name} has won this round.")

                self.player_one.score += 1

            elif self.player_one.current_gesture == 4 and self.computer.current_gesture == 2 or self.computer.choose_gesture == 5:
                print (f"{self.player_one.name} has won this round.")
                self.player_one.score += 1

            elif self.player_one.current_gesture == 5 and self.computer.current_gesture == 1 or self.computer.choose_gesture == 3:
                print (f"{self.player_one.name} has won this round.")
                self.player_one.score += 1

            else:
                print (f"{self.computer.name} has won this round.")
                self.computer.score += 1 
                print()  

               


















    






