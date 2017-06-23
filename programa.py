from PIL import Image
import pymysql
#import pygame,simport easygui as eg
from pygame.locals import *
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

db=pymysql.connect(host="127.0.0.1",user="root",password="expo2017",db="expo2017",autocomit=True)

def exportarimagenesbd(numero):
    foto=None
    c=db.cursor()
    c.execute("select fotosorpresa from sorpresa where idsorpresa=numero;")#crear procedure para abrir imagen
    for ruta in c:
        foto=Image.open(ruta)

#guardar imagen(inserts)(guardar en el disco)
#contar fotos de la base

def guardarimagenendisco(foto):
    eg.msgbox(foto, "fileopenbox", ok_button="Continuar")
    extension = ["*.py", "*.pyc"]
    foto = eg.filesavebox(msg="Guardar archivo",
                             title="Control: filesavebox",
                             default='/home/alumno/Documentos',
                             filetypes=extension
                             )

    eg.msgbox(foto, "filesavebox", ok_button="Continuar")

def guardarimagenenbd(foto):
    c=db.cursor()
    c.execute("insert into personas_fototomada fototomada(foto)")


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
            fondo = pygame.image.load("/home/alumno/Descargas/images.jpeg").convert()
            screen.blit(fondo, (0, 0))# Indicamos la posicion de las "Surface" sobre la ventana
            pygame.display.flip()# se muestran lo cambios en pantalla

main()
