import pygame
from pygame.locals import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((1360, 768))  # pygame.FULLSCREEN)
    reloj = pygame.time.Clock()
    reloj.tick(60)
    frames_totales = 0
    segundo = 0
    variable1=False
    while True:
        if frames_totales % 60 == 0:
            segundo += 1
        frames_totales += 1
        print(segundo)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_TAB:
                    variable1=True
                    print("dentro del segundo while")

                if event.key == K_ESCAPE:
                    exit()
                    pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()

        while variable1==True:
            if frames_totales % 60 == 0:
                segundo += 1
            frames_totales += 1
            print(segundo)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_TAB:
                        variable1 = False
                        print ("dentro del primer while ")

                    if event.key == K_ESCAPE:
                        exit()
                        pygame.quit()
                if event.type == pygame.QUIT:
                    pygame.quit()
