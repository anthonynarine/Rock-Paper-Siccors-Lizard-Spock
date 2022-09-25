from random import randint

class Player:
    def __init__(self):
        self.gesture_option = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.current_gesture = 0
        self.score = 0
        self.tie = 0
      
    