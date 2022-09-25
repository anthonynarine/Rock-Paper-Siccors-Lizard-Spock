from random import randint
from player import Player

class Human(Player):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def choose_gesture(self):
        self.current_gesture = int(input ("Select your weapon of choice:\n[1] for Rock.\n[2] for Paper.\n[3] for Scissors.\n[4] for lizard.\n[5] for spock. \n"))      
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







