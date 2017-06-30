from PIL import Image
import pymysql
from pygame.locals import *
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

db=pymysql.connect(host="172.16.2.250",user="root",password="alumno",db="las_chicas",autocommit=True)
"""foto=None
c = db.cursor()
consulta = "select fotosorpresa from sorpresa where idsorpresa=" + str(3) + ";"
c.execute(consulta)
for ruta in c:
    foto = ruta
print (foto)"""

c= db.cursor()
#consulta="insert into personas_fototomada values("+"null,"+ "hola/hola"+","+str(1)+");"
#c.execute(consulta)
consulta2="insert into personas_fototomada values("+"NULL,"+ "'hola/hola'"+","+str(1)+");"
c.execute(consulta2)