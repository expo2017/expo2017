import pygame.camera
import pygame.image
from PIL import Image
from PIL.ImageOps import *

pygame.camera.init()
print(pygame.camera.list_cameras())
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()
img = cam.get_image()
pygame.image.save(img, "/home/alumno/Imágenes/fotopersona/photo6.jpg")
img = Image.open("/home/alumno/Imágenes/fotopersona/photo4.jpg")
mirror(img).show()#cada vez que se muestra la imagen espejar

pygame.camera.quit()

