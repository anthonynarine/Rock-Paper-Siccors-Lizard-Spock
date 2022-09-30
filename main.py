from player import Player
from game import Game
from human import Human
from computer import Computer
import time 
import random






def main():
    g = Game()       # Welcomes users
    g.greet_user()   # Greets users
    time.sleep(1)    # stalls so users can read rules
    g.game_rules()
    time.sleep(1.5)    # stalls so users can read rules
    g.creat_player() # create player
    time.sleep(1.5) 
    while True:      #loop battle phasse
        g.battle()
        time.sleep(1.5)
        print ("\n" * 1)
        print (f"{g.player_one.name} score = {g.player_one.score}") #print score to terminal
        print (f"{g.computer.name} score = {g.computer.score}")
        print ("\n" * 1)
        if g.player_one.score == 3:  # first to 3 wins
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"{g.player_one.name} is the winner!!!!!!!!!!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            break
        else:
            if g.computer.score == 3:
                    print("~~~~~~~~~~~~~~~~~~~~~~~")
                    print(f"{g.computer.name} is the winner!!!!!!!")
                    print("~~~~~~~~~~~~~~~~~~~~~~~\n")
                    break

main() 