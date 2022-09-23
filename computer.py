from player import Player
from random import randint


class Computer(Player):

    def __init__(self):
        self.name = "Sentient"
        

    def choose_gesture(self):
        gesture = randint(1,5)

        # if gesture == 1:
        #     print (f"You have selected {self.gesture[0]}")
        # elif gesture == 2:
        #     print (f"You have selected {self.gesture[1]}")
        # elif gesture == 3:
        #     print (f"You have selected {self.gesture[2]}!")
        # elif gesture == 4:
        #     print (f"You have selected {self.gesture[3]}!")
        # elif gesture == 5:
        #     print (f"You have selected {self.gesture[4]}!")
        # else:
        #     print (f"You have selected {self.gesture[5]}!")

c = Computer()

c.choose_gesture()