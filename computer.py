from player import Player
from random import randint


class Computer(Player):

    def choose_gesture(self):
        self.current_gesture = randint(1,5) 
        if self.current_gesture == 1:
            print (f"{self.name} has selected {self.gesture_option[0]}")
        elif self.current_gesture == 2:
            print (f"{self.name} has selected {self.gesture_option[1]}")
        elif self.current_gesture == 3:
            print (f"{self.name} has selected {self.gesture_option[2]}")
        elif self.current_gesture == 4:
            print (f"{self.name} has selected {self.gesture_option[3]}")
        else:
            print (f"{self.name} has selected {self.gesture_option[4]}")   


