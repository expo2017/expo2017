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

db = pymysql.connect(host="172.16.2.250", user="root", password="alumno", db="las_chicas", autocommit=True)
listadedatos = []


def guardarimagenenbd(rutafoto,id):#inserts de las rutas
    c = db.cursor()
    consulta = "insert into persona values("+"null," + " ' "+rutafoto+" ' "+","+str(id)+");"
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
    direccionpersona="/home/pi/Pictures/fotopersona" +numero+".jpg"
    pygame.image.save(img,direccionpersona)
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
            print("Agregue elemento a lista Juego")
            lista.append(item)



def abrirventana():
    pygame.init()
    screen = pygame.display.set_mode((1021, 765))  # pygame.FULLSCREEN)
    pygame.display.set_caption("Not Not")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))


def abrirfoto(screen,ruta,cord1,cord2):
    fondo = pygame.image.load(ruta).convert()
    screen.blit(fondo, (cord1,cord2))  # Indicamos la posicion de las "Surface" sobre la ventana
    pygame.display.flip()  # se muestran lo cambios en pantalla

def comprobarrespuesta(tiempo,direccion1):
    while tiempo>=0:
        if tiempo==0:
            return False
        tiempo=tiempo*0.95
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key == K_q:
                    exit()
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





def main():
    pygame.init()
    screen = pygame.display.set_mode((1021, 765))  #pygame.FULLSCREEN)
    pygame.display.set_caption("Not Not")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    puntos = 0
    extraerdatosdelabase()
    listaenjuego = []
    start = False
    nivel = 1
    gano = True
    while True:

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_TAB]:
            start = True

        while start == True:

            if nivel == 1:
                agregarnivelalista(listaenjuego, 1)
                jugadas = 10
                tiempodelnivel = 15
                print("chau")

            if nivel == 2:
                agregarnivelalista(listaenjuego, 2)
                jugadas = 15
                tiempodelnivel = 10
            """if nivel == 3:
                agregarnivelalista(listaenjuego, 3)
                jugadas = 20
                tiempodelnivel = 5"""
            #CICLO
            while jugadas > 0 and gano == True:
                longitud = len(listaenjuego)-1
                variablerandom = random.randrange(0, longitud, longitud)
                direcciondefoto=listaenjuego[variablerandom].fotodireccion
                fondo = pygame.image.load(direcciondefoto).convert()
                screen.blit(fondo, (0, 0))  # Indicamos la posicion de las "Surface" sobre la ventana
                pygame.display.flip()  # se muestran lo cambios en pantalla
                tiempo = tiempodelnivel
                ciclo = True

                while ciclo == True:
                    if tiempo == 0:
                        ciclo = False

                    tiempo = tiempo - 0.95
                    opcion=pygame.key.get_pressed()
                    if opcion[pygame.K_UP]:
                        if listadedatos[variablerandom].botonarriba == 1:
                            puntos = puntos + 1
                            jugadas = jugadas - 1
                            tiempo = 0
                            ciclo = False
                        else:
                            gano = False
                    if opcion[pygame.K_DOWN]:
                        if listadedatos[variablerandom].botonabajo == 1:
                            puntos = puntos + 1
                            jugadas = jugadas - 1
                            tiempo = 0
                            ciclo = False
                        else:
                            gano = False
                    if opcion[pygame.K_RIGHT]:
                        if listadedatos[variablerandom].botonderecha == 1:
                            puntos = puntos + 1
                            jugadas = jugadas - 1
                            tiempo = 0
                            ciclo = False
                        else:
                            gano = False
                    if opcion[pygame.K_LEFT]:
                        if listadedatos[variablerandom].botonaizquierda == 1:
                            puntos = puntos + 1
                            jugadas = jugadas - 1
                            tiempo = 0
                            ciclo = False
                        else:
                            gano = False
                    if teclas[pygame.K_ESCAPE]:
                        quit()
            #findelciclo
            if nivel == 1 and gano == True and jugadas == 0:
                nivel = 2
            if nivel == 2 and gano == True and jugadas == 0:
                nivel = 3
            """if nivel == 3 and gano == True and jugadas == 0:
                #muestra la pantalla ganoo
            if gano == false:
                #muestralapantallaperdio"""













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

main()