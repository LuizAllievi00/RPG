import pygame
from pygame.locals import *

class CharImage:

    def __init__(self, imagePath, imageSize, imagePosition, rectSize):
        if imageSize != 0:
            self.surface = pygame.transform.scale(pygame.image.load(imagePath).convert_alpha(), imageSize)
        else:
            self.surface = pygame.image.load(imagePath).convert_alpha()
        self.position = [imagePosition[0], imagePosition[1]]
        self.rect = Rect(0, 0, rectSize[0], rectSize[1])

    def setSize(self, imageSize):
        self.surface = pygame.transform.scale(self.surface, imageSize,)

class DiceImage:

    def __init__(self, imagePath, imageSize, imagePosition, rectSize):
        if imageSize != 0:
            self.surface = pygame.transform.scale(pygame.image.load(imagePath).convert_alpha(), imageSize)
        else:
            self.surface = pygame.image.load(imagePath).convert_alpha()
        self.position = [imagePosition[0], imagePosition[1]]
        self.rect = Rect(0, 0, rectSize[0], rectSize[1])

    def setSize(self, imageSize):
        self.surface = pygame.transform.scale(self.surface, imageSize,)

class Image:

    def __init__(self, imagePath, imageSize, imagePosition = [0,0]):
        if imageSize != 0:
            self.surface = pygame.transform.scale(pygame.image.load(imagePath).convert_alpha(), imageSize)
        else:
            self.surface = pygame.image.load(imagePath).convert_alpha()
        self.position = [imagePosition[0], imagePosition[1]]
        self.rect = Rect(imagePosition, (self.surface.get_width(), self.surface.get_height()))

    def setSize(self, imageSize):
        self.surface = pygame.transform.scale(self.surface, imageSize)
        self.rect.width = imageSize[0]
        self.rect.height = imageSize[1]
