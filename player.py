from random import randint

class Player:
    def __init__(self, name="Ai"):
        self.gesture_option = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.name = name  
        self.current_gesture = 0
        self.score = 0
        self.tie = 0


