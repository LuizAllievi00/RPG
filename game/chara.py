class Character:
    """This class defines a character object, that is what the player will controller."""
    def __init__(self, charImage, bag = None, attack = 0, defense = 0, speed = 0, hp = 0, hpImage = None):
        self.image = charImage
        self.actualImage = self.image.rect
        self.bag = bag
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.hp = hp
        if hpImage:
            self.hpImage = hpImage
            self.hpRect = self.hpImage.rect
            self.hpRect.x = self.hp / 10


    def downMovement(self):
        """This method is called while the down button is pressed"""
        self.image.position[1] += self.speed
        self.actualImage.y = 0
        if self.actualImage.x == 0: self.actualImage.x += 33
        elif self.actualImage.x == 33: self.actualImage.x += 33
        elif self.actualImage.x == 66: self.actualImage.x = 0
        else: self.actualImage.x = 0

    def upMovement(self):
        """This method is called while the up button is pressed"""
        self.image.position[1] -= self.speed
        self.actualImage.y = 99
        if self.actualImage.x == 0: self.actualImage.x = 33
        elif self.actualImage.x == 33: self.actualImage.x = 66
        elif self.actualImage.x == 66: self.actualImage.x = 0
        else: self.actualImage.x = 0

    def rightMovement(self):
        """This method is called while the right button is pressed"""
        self.image.position[0] += self.speed
        self.actualImage.y = 66
        if self.actualImage.x == 0: self.actualImage.x += 33
        elif self.actualImage.x == 33: self.actualImage.x += 33
        elif self.actualImage.x == 66: self.actualImage.x = 0
        else: self.actualImage.x = 0

    def leftMovement(self):
        """This method is called while the left button is pressed"""
        self.image.position[0] -= self.speed
        self.actualImage.y = 33
        if self.actualImage.x == 0: self.actualImage.x += 33
        elif self.actualImage.x == 33: self.actualImage.x += 33
        elif self.actualImage.x == 66: self.actualImage.x = 0
        else: self.actualImage.x = 0

class Enemy:

    def __init__(self, enemycharImage, attack, defense, speed, hp):
        self.image = charImage
        self.actualImage = self.image.rect
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.hp = hp
