from PIL import Image
import pymysql
import pygame
from pygame.locals import *
import random
import time

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
    print(foto)
    return foto

"""def guardarimagenendisco(foto):
    eg.msgbox(foto, "fileopenbox", ok_button="Continuar")
    extension = ["*.py", "*.pyc"]
    foto = eg.filesavebox(msg="Guardar archivo",
                             title="Control: filesavebox",
                             default='/home/alumno/Documentos',
                             filetypes=extension
                             )

    eg.msgbox(foto, "filesavebox", ok_button="Continuar")"""

def guardarimagenenbd(rutafoto,opcionsorpresa):#inserts de las rutas
    c=db.cursor()
    consulta="insert into personas_fototomada values("+"null,"+ " ' "+rutafoto+" ' "+","+str(opcionsorpresa)+");"
    c.execute(consulta)

def filtrarruta(ruta):
    rutafiltrada=""
    str(ruta)
    for letra in ruta:
        if letra!="(" and letra!=")" and letra!="," :
            rutafiltrada=rutafiltrada+letra
    return rutafiltrada

def boton():
    boton=random.randint(0,1)
    print(boton)
    return boton

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
            opcionsorpresa=random.randrange(1,4)
            ruta=rutaimagensorpresa(opcionsorpresa)
            rutafiltrada=filtrarruta(ruta)
            fondo = pygame.image.load(rutafiltrada).convert()
            screen.blit(fondo, (0, 0))# Indicamos la posicion de las "Surface" sobre la ventana
            pygame.display.flip()# se muestran lo cambios en pantalla
            time.sleep(3)

main()
