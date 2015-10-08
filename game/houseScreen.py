import pygame
from pygame.locals import *
from image import *
from chara import *
from bag import *
from dice import *
import firstScreen
def main(character, winner = False):
    pygame.init();
    mainScreen = pygame.display.set_mode((800, 600), FULLSCREEN);
    mainScreenBG = Image("../images/maps/house_map.png", (800, 600), (0,0));
    clock = pygame.time.Clock();
    ironMan = Character(CharImage('../images/characters/ferro.png', 0, (400,300), (30, 30)));
    dice = Dice(DiceImage("../images/items/dice.png",0, [700,500], [25,32] ));
    key = Image("../images/items/key.png", (30,30), (420,100));
    if not winner : message = 1;
    else: message = 3;
    printKey, printDice = False, False;
    while True:
        
        pygame.display.update();
        keys = pygame.key.get_pressed();
        if keys[K_DOWN]:character.downMovement();
        elif keys[K_UP]:character.upMovement();
        elif keys[K_LEFT]:character.leftMovement();
        elif keys[K_RIGHT]:character.rightMovement();

        for event in pygame.event.get():
            if event.type == QUIT: break;
            if event.type == KEYDOWN:
                if event.key == K_SPACE:dice.anime = True;
                if event.key == K_RETURN and message <= 4: message += 1;
                if key.rect.collidepoint(character.image.position) and event.key == K_e:
                    character.bag.add_item("key", "slot1");
                    printKey = False;
                    pygame.display.update();
                    character.image.position = [500,350];
                    firstScreen.main(character, False, False, True);
                if(Rect(610,350,300,600).collidepoint(character.image.position) and not printDice): printDice = True;

        mainScreen.blit(mainScreenBG.surface, mainScreenBG.position);
        mainScreen.blit(ironMan.image.surface, ironMan.image.position, ironMan.image.rect);
        mainScreen.blit(character.image.surface, character.image.position, character.image.rect);

        if dice.anime:
            for i in range(300):
                result = dice.diceAnimation();
                mainScreen.blit(dice.diceImage, dice.dicePosition, dice.diceRect);
                pygame.display.update();
            if result == 6: result = None; printKey = True;
            dice.anime = False;
        elif printDice: mainScreen.blit(dice.diceImage, dice.dicePosition, dice.diceRect);

        if printKey: mainScreen.blit(key.surface, key.position); pygame.display.update();

        if message <= 2:
            mainScreen = showMessage(mainScreen, message);
            pygame.display.update();

        if winner and message <= 4:
            mainScreen = showMessage(mainScreen, message)
            pygame.display.update()
        pygame.display.update();
        time_passed = clock.tick(12);



def showMessage(screen, message):
    if message == 1:
        message = Image("../images/messages/kingMessage1.png" ,0, (0,400));
        screen.blit(message.surface, message.position);
        return screen;
    elif message == 2:
        message = Image("../images/messages/kingMessage2.png",0, (0,400));
        screen.blit(message.surface, message.position);
        return screen;
    elif message == 3:
        message = Image("../images/messages/backingKingMessage1.png",0, (0,400));
        screen.blit(message.surface, message.position);
        return screen;
    elif message == 4:
        message = Image("../images/messages/backingKingMessage2.png",0, (0,400));
        screen.blit(message.surface, message.position);
        return screen;
