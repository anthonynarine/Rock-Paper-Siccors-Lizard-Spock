from player import Player
from random import randint


class Computer(Player):
    def __init__(self,name = "Ai"):
        super().__init__()
        self.name = name

    def choose_gesture(self):
        self.current_gesture = randint(1,5) 
        if self.current_gesture == 1:
            print (f"You have selected {self.gesture_option[0]}")
        elif self.current_gesture == 2:
            print (f"You have selected {self.gesture_option[1]}")
        elif self.current_gesture == 3:
            print (f"You have selected {self.gesture_option[2]}")
        elif self.current_gesture == 4:
            print (f"You have selected {self.gesture_option[3]}")
        else:
            print (f"You have selected {self.gesture_option[4]}")   


