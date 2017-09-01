from PIL import Image
import pygame
from pygame.locals import *
import pygame.image
import time
import sys

def main():

    while True:
        # Initialise screen
        pygame.init()
        screen = pygame.display.set_mode((1021,765),pygame.FULLSCREEN)
        pygame.display.set_caption('hola')

        # Fill background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        # Display some text
        #font = pygame.font.Font(None, 36)
        #text = font.render("Hello There", 1, (10, 10, 10))
        #textpos = text.get_rect()
        #textpos.centerx = background.get_rect().centerx
        #background.blit(text, textpos)
        # Blit everything to the screen

        fondo = pygame.image.load("/home/pi/Pictures/Pregunta1.png").convert()
        screen.blit(fondo, (0, 0))
        pygame.display.flip()
        time.sleep(2)
        variable = 5

        while variable>0:
            variable=variable-1
            time.sleep(1)
            fondo = pygame.image.load("/home/pi/Pictures/hola.jpg").convert()
            screen.blit(fondo, (700,0 ))
            pygame.display.flip()


        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type==pygame.K_ESCAPE:
                quit()
            if event.type== QUIT:
                exit()

            if event.type==KEYDOWN:
                if event.key==K_q:
                    exit()


main()