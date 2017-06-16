from PIL import Image
import pymysql
import pygame,sys
from pygame.locals import *
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

#db=pymysql.connect(host="127.0.0.1",user="root",password="expo2017",db="expo2017",autocomit=True)

"""def cargarimagenes():
    foto=None
    c=db.cursor()
    c.execute("select ruta from fotosorpresa;")
    for ruta in c:
        foto=Image.open(ruta)

    listadeimagenessorpresa.append(foto)"""

#def mostrarimagensorpresa(pos):
def boton():
    return True

def main():
    pygame.init()
    screen = pygame.display.set_mode()
    pygame.display.set_caption("Sorpresa")

    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if boton()==True:
            #opcionsorpresa=random.randrange(1,len(listadeimagenessorpresa))
            opcionsorpresa=1
            if opcionsorpresa ==1:
                fondo = pygame.image.load("/home/alumno/Descargas/images.jpeg").convert()

                screen.blit(fondo, (0, 0))# Indicamos la posicion de las "Surface" sobre la ventana
                pygame.display.flip()# se muestran lo cambios en pantalla

main()