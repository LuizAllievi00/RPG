import pygame
from pygame.locals import *
from image import *
from chara import *
from bag import *
import houseScreen
import cavernScreen
import sys
def main(character = None,begin = False, begin2 = False, printCaveMessage = False, printCavern = False, backingKing = False):
    pygame.init();
    mainScreen = pygame.display.set_mode((800, 600), FULLSCREEN);
    mainScreenBG = Image("../images/maps/map.png", (800, 600), (0,0));
    if not character:
        character = Character(CharImage("../images/characters/jailson.png", 0, (0,0), (30,30)), Bag(),20,8,6,1000, CharImage('../images/menus/hpBar.png', 0,(680,30), (300,300)));
    house, cavern = Image("../images/items/house.png", [50,50], [480, 100]), Image("../images/items/cavern.png", [50,50], [350, 380]);
    clock = pygame.time.Clock();
    startMessage1 = Image("../images/messages/startMessage1.png", 0, (0, 400));
    startMessage2 = Image('../images/messages/startMessage2.png', 0, (0,400));
    preCavernMessage = Image('../images/messages/preCavernMessage.png', 0, (0,400));
    posCavernMessage = Image("../images/messages/posCavernMessage.png", 0, (0,400));
    while True:
        if backingKing:
            backingKingAux = True;
            mainScreen.blit(posCavernMessage.surface, posCavernMessage.position);
        else: backingKingAux = False;
        keys = pygame.key.get_pressed();

        if keys[K_DOWN]:character.downMovement();
        elif keys[K_UP]:character.upMovement();
        elif keys[K_LEFT]:character.leftMovement();
        elif keys[K_RIGHT]:character.rightMovement();

        for event in pygame.event.get():
            if event.type == QUIT: break;
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if begin: begin = not begin; begin2 = True;
                    elif begin2: begin2 = not begin2;
                    elif backingKing: backingKing = False
                    elif printCaveMessage: printCaveMessage = False; printCavern = True; print 8
                if event.key == K_ESCAPE: sys.exit();
                if event.key == K_e:
                    if house.rect.collidepoint(character.image.position):houseScreen.main(character, backingKingAux);
                    if cavern.rect.collidepoint(character.image.position):
                        if character.bag.get_item("slot1") == "key":character.image.position = [780, 300]; cavernScreen.main(character);

        mainScreen.blit(mainScreenBG.surface, mainScreenBG.position);

        if begin:
            mainScreen.blit(startMessage1.surface, startMessage1.position);
            pygame.display.update();
        elif begin2:
            mainScreen.blit(startMessage2.surface, startMessage2.position);
            pygame.display.update();
        elif printCaveMessage:
            mainScreen.blit(preCavernMessage.surface, preCavernMessage.position);
            pygame.display.update();
        else:
            mainScreen.blit(house.surface, house.position);

        if printCavern:
            mainScreen.blit(cavern.surface, cavern.position);

        mainScreen.blit(character.image.surface, character.image.position, character.image.rect);

        pygame.display.update();
        time_passed = clock.tick(12);
