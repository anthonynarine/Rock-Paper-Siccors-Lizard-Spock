from player import Player


class Human (Player):
    #Human player instances will have names.
    def __init__(self, name):
        self.name = name
        
    def choose_gesture(self):
        gesture = int(input ("Select your weapon of choice:\n[1] for Rock.\n[2] for Paper.\n[3] for Scissors.\n[4] for lizard.\n[5] for spock. \n"))

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
