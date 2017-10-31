import pygame
from pygame.locals import *

def abrirfoto(screen, ruta, cord1, cord2):
    fondo = pygame.image.load(ruta).convert()
    screen.blit(fondo, (cord1, cord2))  # Indicamos la posicion de las "Surface" sobre la ventana
    pygame.display.update()  # se muestran lo cambios en pantalla


def main():
    pygame.init()
    screen = pygame.display.set_mode((120, 70))  # pygame.FULLSCREEN)
    pygame.display.set_caption("Not Not")
    reloj = pygame.time.Clock()

    frames_totales = 0
    segundo = 0
    variable1=False
    reloj.tick(60)

    while True:
        

        for event in pygame.event.get():
            print("hola")
            if event.type == pygame.KEYDOWN:
                if event.key == K_TAB:
                    frames_totales = 0
                    segundo = 0
                    print("dentro del segundo while")
                    variable1 = True

                if event.key == K_ESCAPE:
                    exit()
                    pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()

        reloj.tick(60)

        if frames_totales % 60 == 0:
            segundo += 1
            print(segundo)
        frames_totales += 1

        while variable1==True:
            reloj.tick(60)
            if frames_totales % 60 == 0:
                segundo += 1
                print(segundo)
            frames_totales += 1


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_TAB:
                        variable1 = False
                        print ("dentro del primer while ")
                        frames_totales = 0
                        segundo = 0

                    if event.key == K_ESCAPE:
                        exit()
                        pygame.quit()
                if event.type == pygame.QUIT:
                    pygame.quit()

main()