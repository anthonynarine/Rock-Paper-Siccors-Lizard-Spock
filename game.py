

from human import Human
from computer import Computer
import random


class Game:
   
    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.computer = None

        
    # def greet_user(self):
    #     print("-------------------------------------------------------------")
    #     welcome = f"Welcome to Rock ~ Paper ~ Scissors ~ Lizard ~ Spock!\n"
    #     welcome += f"\nEach match will be best of the 3 rounds\n"
    #     welcome += f"Use the number keys to enter your selection"
    #     print(welcome)
    #     print("-------------------------------------------------------------")


    # def game_rules(self):

    #     print("------------------------------------------------------------")
    #     print("The game rules are as follows:")
    #     rules = "\nScissors cuts paper and slices Lizard.\n"
    #     rules += "Paper smuthers Rock and vanquishes Spock.\n"
    #     rules += "Rock crushes Lizard and breaks Scissors.\n"
    #     rules += "Lizard eats Paper and Poisons Spock.\n"
    #     rules += "Spock vaporizes Rock and smashes scissors.\n"
    #     print (rules)
    #     print("------------------------------------------------------------")

    def creat_player(self):
        # number_of_player = int(input(("How many players will we have today?\n1 ~ 2 or 3 for a surprise  ")))
        # if number_of_player == 1:
            name = input ("Enter your name player: ")
            self.player_one = Human(name)
            self.computer = Computer()
            
    def battle(self):
        while True:
            
            self.player_one.choose_gesture()
            self.computer.choose_gesture()

            if self.player_one.current_gesture == self.computer.current_gesture:
                print ("Its a tie, next round")

            elif self.player_one.current_gesture == 1 and self.computer.current_gesture == 3 or self.computer.choose_gesture == 4:
                print("#" * 20)
                print (f"{self.player_one.name} has won this round.")
                print("#" * 20)
                self.player_one.score += 1

            elif self.player_one.current_gesture == 2 and self.computer.current_gesture == 1 or self.computer.choose_gesture == 5:
                print("#" * 20)
                print (f"{self.player_one.name} has won this round.")
                print("#" * 20)
                self.player_one.score += 1

            elif self.player_one.current_gesture == 3 and self.computer.current_gesture == 2 or self.computer.choose_gesture == 4:
                print("#" * 20)
                print (f"{self.player_one.name} has won this round.")
                print("#" * 20)
                self.player_one.score += 1

            elif self.player_one.current_gesture == 4 and self.computer.current_gesture == 2 or self.computer.choose_gesture == 5:
                print("#" * 20)
                print (f"{self.player_one.name} has won this round.")
                print("#" * 20)
                self.player_one.score += 1

            elif self.player_one.current_gesture == 5 and self.computer.current_gesture == 1 or self.computer.choose_gesture == 3:
                print("#" * 20)
                print (f"{self.player_one.name} has won this round.")
                self.player_one.score += 1

            else:
                print (f"{self.computer.name} has won this round.")
                self.computer.score += 1
                
            print (f"{self.player_one.name} score = {self.player_one.score}")
            print (f"{self.computer.name} score = {self.computer.score}")
            if self.player_one.score == 3:
                print(f"{self.player_one.name} is the winner")
                break
            else:
                if self.computer.score == 3:
                    print(f"{self.player_one.name} is the winner")
                    break
                

    # def score_total(self):
    #     while True:

    #             self.battle()
    #         else:
    #             break

            









g = Game()
# g.greet_user()
# g.game_rules()
g.creat_player()
g.battle()















    






