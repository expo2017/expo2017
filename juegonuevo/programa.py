from clases.direccion import direccion
from PIL import Image
import pymysql
import pygame
from pygame.locals import *
import random
import time
import pygame.image
import pygame.camera
import sys

db=pymysql.connect(host="172.16.2.250",user="root",password="alumno",db="las_chicas",autocommit=True)
listadedatos=[]

def guardarimagenenbd(rutafoto,opcion):#inserts de las rutas
    c=db.cursor()
    consulta="insert into personas_fototomada values("+"null,"+ " ' "+rutafoto+" ' "+","+str(opcion)+");"
    c.execute(consulta)

def tomarfoto():
    pygame.camera.init()
    print(pygame.camera.list_cameras())
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    cam.start()
    img = cam.get_image()
    #funcionguardardentrodeestoconuncountdefototomada
    pygame.camera.quit()

def datosdelabase():
    nuevadirreccion=direccion()
    c = db.cursor()
    c.execute("select * from direccion;")
    for item in c:
        nuevadirreccion.setid(item[0])
        nuevadirreccion.setfoto(item[1])
        nuevadirreccion.setarriba(item[2])
        nuevadirreccion.setabajo(item[3])
        nuevadirreccion.setderecha(item[4])
        nuevadirreccion.setizquierda(item[5])
        nuevadirreccion.setcondicion(item[6])
        nuevadirreccion.setnivel(item[7])
        listadedatos.append(nuevadirreccion)
        print(item)
def main():
    pygame.init()
    screen = pygame.display.set_mode((1021, 765), pygame.FULLSCREEN)
    pygame.display.set_caption("Not Not")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.K_ESCAPE:
                quit()
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_q:
                    exit()


datosdelabase()