import random
class Dice:
    def __init__(self, diceImage):
        self.diceImage = diceImage.surface
        self.diceRect = diceImage.rect
        self.dicePosition = diceImage.position
        self.anime = False
        self.diceResults = {result : x + 1 for x,result in enumerate(range(0,150,25))}
    def diceAnimation(self):
        self.diceRect.x = random.choice(range(0,150,25))
        return self.diceResults[self.diceRect.x]
