import pygame
import battleScreen
from pygame.locals import *
from image import *
from chara import *
from bag import *
from dice import *

def main(character):
    pygame.init()
    mainScreen = pygame.display.set_mode((800, 600), FULLSCREEN)
    mainScreenBG = Image("../images/maps/cavern_map.png", (800, 600), (0,0))
    clock = pygame.time.Clock()
    boss = Character(CharImage('../images/characters/boss.png', 0, (400,300), (30, 30)), None, 20, 8, 0, 1000, CharImage('../images/menus/hpBar.png', 0,(30,30), (100,100)) )
    dice = Dice(DiceImage("../images/items/dice.png",0, [700,500], [25,32] ))
    message = 1
    while True:


        keys = pygame.key.get_pressed()
        if keys[K_DOWN]:character.downMovement()
        elif keys[K_UP]:character.upMovement()
        elif keys[K_LEFT]:character.leftMovement()
        elif keys[K_RIGHT]:character.rightMovement()

        for event in pygame.event.get():
            if event.type == QUIT: break
            if event.type == KEYDOWN:
                if event.key == K_RETURN: message += 1;
                if event.key == K_SPACE:dice.anime = True

        mainScreen.blit(mainScreenBG.surface, mainScreenBG.position)
        mainScreen.blit(boss.image.surface, boss.image.position, boss.image.rect)
        mainScreen.blit(character.image.surface, character.image.position, character.image.rect)

        if message <= 3:
            mainScreen = showMessage(mainScreen, message);
            pygame.display.update();
        else: battleScreen.main(character, boss)

        pygame.display.update()
        time_passed = clock.tick(12)
def showMessage(screen, message):
    if message == 1:
        message = Image("../images/messages/cavernMessage1.png" ,0, (0,400));
        screen.blit(message.surface, message.position);
        return screen;
    elif message == 2:
        message = Image("../images/messages/cavernMessage2.png",0, (0,400));
        screen.blit(message.surface, message.position);
        return screen;
    elif message == 3:
        message = Image("../images/messages/cavernMessage3.png",0, (0,400));
        screen.blit(message.surface, message.position);
        return screen;
