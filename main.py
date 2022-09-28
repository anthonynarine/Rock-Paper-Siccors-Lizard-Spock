from player import Player
from game import Game
from human import Human
from computer import Computer
import time 
import random






def main():
    g = Game()
    g.greet_user()
    time.sleep(3)
    g.game_rules()
    g.creat_player()
    time.sleep(1.5) 
    while True:
        g.battle()
        time.sleep(2)
        print ("\n" * 1)
        print (f"{g.player_one.name} score = {g.player_one.score}")
        print (f"{g.computer.name} score = {g.computer.score}")
        print ("\n" * 1)
        if g.player_one.score == 3:
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