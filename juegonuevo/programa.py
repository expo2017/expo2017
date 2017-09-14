from .clases.direccion import direccion
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
def datosdelabase():
    nuevadirreccion=direccion()
    c = db.cursor()
    c.execute("select * from direccion;")
    for item in c:
        nuevadirreccion.setid(item[1])
        nuevadirreccion.setfoto(item[2])
        nuevadirreccion.setarriba(item[3])
        nuevadirreccion.setabajo(item[4])
        nuevadirreccion.setderecha(item[5])
        nuevadirreccion.setizquierda(item[6])
        nuevadirreccion.setcondicion(item[7])
        nuevadirreccion.setnivel(item[8])
        listadedatos.append(nuevadirreccion)


datosdelabase()