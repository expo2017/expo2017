from PIL import Image
import pymysql
import pygame
from pygame.locals import *
import random
import time
import pygame.image
import pygame.camera
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

db=pymysql.connect(host="172.16.2.250",user="root",password="alumno",db="las_chicas",autocommit=True)

def rutaimagenpregunta(numero):#devuelve la ruta de la imagen sorpresa(se le pasa por parametro la opcion random
    foto=None
    rutafiltrada = ""
    c=db.cursor()
    consulta="select fotopregunta from pregunta where idpregunta="+str(numero)+";"
    c.execute(consulta)
    for ruta in c:
        foto=ruta

    for letra in foto:
        if letra != "(" and letra != ")" and letra != "," and letra!= "'":
            rutafiltrada = rutafiltrada + letra
    return rutafiltrada

def consultarespuesta(id):
    respuesta=None
    respuestafiltrada=""
    c = db.cursor()
    consulta = "select respuesta from pregunta where idpregunta=" + str(id) + ";"
    c.execute(consulta)
    for x in c:
        respuesta=x

    for letra in respuesta:
        if letra != "(" and letra != ")" and letra != "," and letra!= "'":
             respuestafiltrada= respuestafiltrada + letra

    return respuestafiltrada

def contarpreguntas():
    preguntas = None
    cantidadfiltrada = 0
    c = db.cursor()
    consulta = "select count(idpregunta) from pregunta;"
    c.execute(consulta)
    for x in c:
        preguntas = x

    for letra in preguntas:
        if letra != "(" and letra != ")" and letra != "," and letra != "'":
             cantidadfiltrada= cantidadfiltrada + letra

    print(cantidadfiltrada)
    return cantidadfiltrada

def guardarimagenenbd(rutafoto,opcion):#inserts de las rutas
    c=db.cursor()
    consulta="insert into personas_fototomada values("+"null,"+ " ' "+rutafoto+" ' "+","+str(opcion)+");"
    c.execute(consulta)

def guardarimagenendisco(nombre,img):
    ruta="/home/alumno/Imágenes/Foto_persona/"+ str(nombre)
    pygame.image.save(img,ruta)

def tomarfoto():
    pygame.camera.init()
    print(pygame.camera.list_cameras())
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    cam.start()
    img = cam.get_image()
    pygame.camera.quit()
    return img

def main():
    pygame.init()
    screen = pygame.display.set_mode((1021,765),pygame.FULLSCREEN)
    pygame.display.set_caption("Pregunta")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    boton = None
    botonrespuesta = None
    puntaje=None
    limite=contarpreguntas()

    while True:
        # Posibles entradas del teclado y mouse
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

        if boton==True:
            opcion=opcion+1
            respuestacorrecta=None
            if(opcion>limite):
                #mostarfotopersona y si gano o no con puntaje
                #volver todas las variables al valor original
                boton == False
            else :
                ruta=rutaimagenpregunta(opcion)
                fondo = pygame.image.load(ruta).convert()
                screen.blit(fondo, (0, 0))# Indicamos la posicion de las "Surface" sobre la ventana
                pygame.display.flip()# se muestran lo cambios en pantalla
                respuestacorrecta=consultarespuesta(opcion)
                #definir limitedetiempo
                #while(limitar)
                if botonrespuesta==respuestacorrecta:
                    puntaje=puntaje+1
                    #imagendecorrecto
                    #limitedetiempo=0

        #if boton==False:
            #abreimagenprincipal


main()
