from PIL import Image
import pymysql
import pygame
from pygame.locals import *
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

db=pymysql.connect(host="172.16.2.250",user="root",password="alumno",db="las_chicas",autocommit=True)

def rutaimagensorpresa(numero):#devuelve la ruta de la imagen sorpresa(se le pasa por parametro la opcion random
    foto=None
    c=db.cursor()
    consulta="select fotosorpresa from sorpresa where idsorpresa="+str(numero)+";"
    c.execute(consulta)
    for ruta in c:
        foto=ruta
    return foto

#guardar imagen(inserts)(guardar en el disco)
#contar fotos de la base

"""def guardarimagenendisco(foto):
    eg.msgbox(foto, "fileopenbox", ok_button="Continuar")
    extension = ["*.py", "*.pyc"]
    foto = eg.filesavebox(msg="Guardar archivo",
                             title="Control: filesavebox",
                             default='/home/alumno/Documentos',
                             filetypes=extension
                             )

    eg.msgbox(foto, "filesavebox", ok_button="Continuar")"""

def guardarimagenenbd(rutafoto,opcionsorpresa):
    c=db.cursor()
    consulta="insert into personas_fototomada values("+"null,"+ " ' "+rutafoto+" ' "+","+str(opcionsorpresa)+");"
    c.execute(consulta)


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
            fondo = pygame.image.load("/home/alumno/Imágenes/Foto_sorpresa/images.jpeg").convert()
            screen.blit(fondo, (0, 0))# Indicamos la posicion de las "Surface" sobre la ventana
            pygame.display.flip()# se muestran lo cambios en pantalla

main()
