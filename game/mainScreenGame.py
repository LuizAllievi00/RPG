import pygame
from pygame.locals import *
from image import Image
import firstScreen
import sys
def main():
    pygame.init()
    mainScreen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), FULLSCREEN)
    mainScreenBG_image1 = Image("../images/menus/castelo_menu.png", (pygame.display.Info().current_w, pygame.display.Info().current_h), (0,0))
    mainScreenBG_image2 = Image("../images/menus/folhas_menu.png", (pygame.display.Info().current_w, pygame.display.Info().current_h), (0,0))
    play = (Image("../images/menus/play_image.png",(300,105), (900,175)))
    exit = (Image("../images/menus/exit_image.png",(300,105), (900,425)))
    tutorial = (Image("../images/menus/tutorial_image.png", (300,105),(900,300)))
    pygame.mixer.music.load('../sounds/music.mp3')
    pygame.mixer.music.play(-1)



    while True:
        for event in pygame.event.get():
            if event.type == QUIT: break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.rect.collidepoint(pygame.mouse.get_pos()):
                    firstScreen.main(None, True)
                if exit.rect.collidepoint(pygame.mouse.get_pos()): sys.exit()
        mainScreen.blit(mainScreenBG_image1.surface, mainScreenBG_image1.position)
        mainScreen.blit(mainScreenBG_image2.surface, mainScreenBG_image2.position)
        mainScreen.blit(play.surface, play.position)
        mainScreen.blit(exit.surface, exit.position)

        pygame.display.update()
main()
