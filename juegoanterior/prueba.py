import pymysql
import pygame
from pygame.locals import *
db=pymysql.connect(host="172.16.2.250",user="root",password="alumno",db="las_chicas",autocommit=True)

def rutaimagensorpresa(numero):#devuelve la ruta de la imagen sorpresa(se le pasa por parametro la opcion random
    foto=None
    rutafiltrada = ""
    c=db.cursor()
    consulta="select fotosorpresa from sorpresa where idsorpresa="+str(numero)+";"
    c.execute(consulta)
    for ruta in c:
        foto=ruta

    for letra in foto:
        if letra != "(" and letra != ")" and letra != "," and letra!= "'":
            rutafiltrada = rutafiltrada + letra
    print(rutafiltrada)
    return rutafiltrada

def main():
    pygame.init()
    screen = pygame.display.set_mode()
    pygame.display.set_caption("Sorpresa")

    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


            opcionsorpresa=1
            ruta=rutaimagensorpresa(opcionsorpresa)
            fondo = pygame.image.load(ruta).convert()
            screen.blit(fondo, (0, 0))# Indicamos la posicion de las "Surface" sobre la ventana
            pygame.display.flip()# se muestran lo cambios en pantalla


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

    print(respuestafiltrada)
    return respuestafiltrada

consultarespuesta(4)