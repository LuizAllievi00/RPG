cdimport pygame
import firstScreen
import sys
from pygame.locals import *
from image import *
from chara import *
from bag import *
from dice import *
import time

def showMessage(screen, message):
    if message == 1:
        message = Image("../images/messages/kingMessage1.png" ,0, (0,400));
        screen.blit(message.surface, message.position);
        return screen;
    elif message == 2:
        message = Image("../images/messages/winnerMessage.png" ,0, (0,400));
        screen.blit(message.surface, message.position);
        return screen;
    elif message == 3:
        message = Image("../images/messages/loserMessage.png" ,0, (0,400));
        screen.blit(message.surface, message.position);
        return screen;

def diceAnime(dice, screen, fighter1, fighter2):
    result = dice.diceAnimation();
    screen.blit(dice.diceImage, dice.dicePosition, dice.diceRect);
    screen.blit(fighter1.image.surface, fighter1.image.position, fighter1.image.rect)
    screen.blit(fighter1.hpImage.surface, fighter1.hpImage.position, fighter1.hpRect)
    screen.blit(fighter2.image.surface, fighter2.image.position, fighter2.image.rect)
    screen.blit(fighter2.hpImage.surface, fighter2.hpImage.position, fighter2.hpRect)
    return (dice, screen, fighter1, fighter2, result)

def main(fighter1, fighter2):
    pygame.init()
    mainScreen = pygame.display.set_mode((800, 600), FULLSCREEN)
    mainScreenBG = Image("../images/maps/cavern_map.png", (800, 600), (0,0))
    clock = pygame.time.Clock()
    dice = Dice(DiceImage("../images/items/dice.png",0, [400,300], [25,32] ))
    message = 1
    turn, result, printDice, dice.anime, gameOver = True, False, False,False, False;
    fighter1.image.position, fighter1.image.rect.x, fighter1.image.rect.y = [700,300],0,33 ;
    fighter2.image.position,fighter2.image.rect.x, fighter2.image.rect.y = [100,300],0, 66;
    dice.dicePosition = [400,300];
    while True:

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT: break
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    message += 1;
                    if message == 3: gameOver = True
                if event.key == K_SPACE:dice.anime = True


        mainScreen.blit(mainScreenBG.surface, mainScreenBG.position);
        if dice.anime:
            for i in range(300):
                dice, mainScreen, fighter1, fighter2, result  = diceAnime(dice, mainScreen, fighter1, fighter2)
                pygame.display.update()
            dice.anime = False;

        elif printDice: mainScreen.blit(dice.diceImage, dice.dicePosition, dice.diceRect);

        if result:
            if turn:
                fighter1.hp -= (fighter2.attack * result) - fighter1.defense
                fighter1.hpRect.x = fighter1.hp / 10
                turn = not turn
                result = None
            else:
                dice.anime = True
                fighter2.hp -= (fighter1.attack * result) - fighter2.defense
                fighter2.hpRect.x = fighter2.hp / 10
                turn = not turn
                result = None

        if message <= 1:
            mainScreen = showMessage(mainScreen, message);
            pygame.display.update();
        else: printDice = True

        if  fighter2.hp <= 0:
            message = 2
            mainScreen = showMessage(mainScreen, message)
            pygame.display.update()
            time.sleep(2)
            firstScreen.main(fighter1, False, False, False, False, True)

        elif fighter1.hp <= 0:
            message = 3
            mainScreen = showMessage(mainScreen, message)
            pygame.display.update()
            time.sleep(3)
            gameOver = True
            if gameOver: sys.exit()

        mainScreen.blit(fighter1.image.surface, fighter1.image.position, fighter1.image.rect)
        mainScreen.blit(fighter1.hpImage.surface, fighter1.hpImage.position, fighter1.hpRect)
        mainScreen.blit(fighter2.image.surface, fighter2.image.position, fighter2.image.rect)
        mainScreen.blit(fighter2.hpImage.surface, fighter2.hpImage.position, fighter2.hpRect)

        pygame.display.update()
        time_passed = clock.tick(12)
