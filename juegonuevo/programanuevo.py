from clases.direccion import direccion
from clases.nivel import nivel
from clases.juego import juego
from PIL import Image
import pymysql
import pygame
from pygame.locals import *
import random
from random import randint
import time
import pygame.image
import pygame.camera
import sys

db = pymysql.connect(host="172.16.2.250", user="root", password="alumno", db="las_chicas", autocommit=True)
listadedatos = []


def guardarimagenenbd(rutafoto, id):  # inserts de las rutas
    c = db.cursor()
    consulta = "insert into persona values(" + "null," + " ' " + rutafoto + " ' " + "," + str(id) + ");"
    c.execute(consulta)


def tomarfoto():
    numero = 0
    pygame.camera.init()
    print(pygame.camera.list_cameras())
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    c = db.cursor()
    consulta = "select count(idpersona)from persona; "
    c.execute(consulta)
    for item in c:
        numero = item
    cam.start()
    img = cam.get_image()
    direccionpersona = "/home/pi/Pictures/fotopersona" + numero + ".jpg"
    pygame.image.save(img, direccionpersona)
    pygame.camera.quit()


def extraerdatosdelabase():
    c = db.cursor()
    c.execute("select * from direccion;")
    for item in c:
        nuevadirreccion = direccion()
        nuevadirreccion.setid(item[0])
        nuevadirreccion.setfoto(item[1])
        nuevadirreccion.setarriba(item[2])
        nuevadirreccion.setabajo(item[3])
        nuevadirreccion.setderecha(item[4])
        nuevadirreccion.setizquierda(item[5])
        nuevadirreccion.setcondicion(item[6])
        nuevadirreccion.setnivel(item[7])
        listadedatos.append(nuevadirreccion)


def agregarnivelalista(lista, n):
    for item in listadedatos:
        if item.nivel == n:
            lista.append(item)

def abrirfoto(screen, ruta, cord1, cord2):
    fondo = pygame.image.load(ruta).convert()
    screen.blit(fondo, (cord1, cord2))  # Indicamos la posicion de las "Surface" sobre la ventana
    pygame.display.flip()  # se muestran lo cambios en pantalla


def comprobarrespuesta(tiempo, direccion1):
    while tiempo >= 0:
        if tiempo == 0:
            return False
        pygame.time.delay(1000)
        tiempo-=1
        print(tiempo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    if direccion1.botonarriba == 1:
                        return True
                    else:
                        return False
                if event.key == K_DOWN:
                    if direccion1.botonabajo == 1:
                        return True
                    else:
                        return False
                if event.key == K_LEFT:
                    if direccion1.botonizquierda == 1:
                        return True
                    else:
                        return False
                if event.key == K_RIGHT:
                    if direccion1.botonderecha == 1:
                        return True
                    else:
                        return False
                if event.key == K_ESCAPE:
                    exit()
                    pygame.quit()

def crearniveles(juego1):
    nivel1=nivel()
    nivel1.setid(1)
    nivel1.settiempo(11)
    nivel1.setjugadas(10)
    juego1.setnivel(nivel1)

    nivel2 = nivel()
    nivel2.setid(2)
    nivel2.settiempo(8)
    nivel2.setjugadas(15)
    juego1.setnivel(nivel2)

    nivel3 = nivel()
    nivel3.setid(3)
    nivel3.settiempo(5)
    nivel3.setjugadas(20)
    juego1.setnivel(nivel3)

def fondodecolor(screen,opcion):
    if opcion==1:#blanco
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        pygame.display.flip()
    if opcion==2:#negro
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        pygame.display.flip()
    if opcion==3:#verde
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 204, 0))
        screen.blit(background, (0, 0))
        pygame.display.flip()
    if opcion==4:#rojo
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((204, 51, 0))
        screen.blit(background, (0, 0))
        pygame.display.flip()




def main():
    extraerdatosdelabase()
    pygame.init()
    screen = pygame.display.set_mode((1360,768))  # pygame.FULLSCREEN)
    pygame.display.set_caption("Not Not")

    juegonuevo=juego()
    crearniveles(juegonuevo)

    while True:
        fondodecolor(screen, 1)
        abrirfoto(screen,"/home/pi/Pictures/fotointerfaz/acercate1.png",150,0)
        pygame.time.delay(1000)
        fondodecolor(screen, 2)
        abrirfoto(screen, "/home/pi/Pictures/fotointerfaz/acercate2.png",150,0)
        pygame.time.delay(1000)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_TAB:
                    fondodecolor(screen, 1)
                    juegonuevo.setstart(True)
                    juegonuevo.setnivelactual(juego.niveles[0])
                if event.key == K_ESCAPE:
                    exit()
                    pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()





        """teclas = pygame.key.get_pressed()
        if teclas[pygame.K_TAB]:
            juegonuevo.setstart(True)
            juegonuevo.setnivelactual(juego.niveles[0])"""

        while juegonuevo.start==True:
            #imagendeempiezaeljuego
            agregarnivelalista(juegonuevo.listadedirecciones,juegonuevo.nivelactual.id)

            while juegonuevo.nivelactual.jugadas>0 and juegonuevo.gano==True:
                longitud = len(juegonuevo.listadedirecciones)-1
                variablerandom = random.randint(0, longitud)
                direcciondefoto = juegonuevo.listadedirecciones[variablerandom].fotodireccion
                fondodecolor(screen,1)
                abrirfoto(screen,direcciondefoto,0,0)

                juegonuevo.gano=comprobarrespuesta(juegonuevo.nivelactual.tiempo,juegonuevo.listadedirecciones[variablerandom])
                juegonuevo.nivelactual.jugadas-=1

                fondodecolor(screen,3)
                pygame.time.delay(1000)



            if juegonuevo.gano==False:
                fondodecolor(screen, 3)
                pygame.time.delay(1000)
                abrirfoto(screen,"/home/pi/Pictures/fotointerfaz/perdiste.jpg",0,0)
                juegonuevo.setstart(False)

            if juegonuevo.nivelactual.jugadas==0:
                idaux=juegonuevo.nivelactual.id+1
                for nivel in juegonuevo.niveles:
                    if nivel.id==idaux:
                        juegonuevo.nivelactual=nivel

            if juegonuevo.nivelactual.jugadas==0 and juegonuevo.nivelactual.id==3:
                abrirfoto(screen, "/home/pi/Pictures/fotointerfaz/ganaste.jpg", 0, 0)
                juegonuevo.setstart(False)













main()