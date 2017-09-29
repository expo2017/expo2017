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
        screen = pygame.display.set_mode((1021,765))
        pygame.display.set_caption('hola')

        # Fill background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((240, 40 , 0))
        screen.blit(background, (0, 0))
        pygame.display.flip()
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