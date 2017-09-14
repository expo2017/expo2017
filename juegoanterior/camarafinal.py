import pygame.camera
import pygame.image
from PIL import Image
from PIL.ImageOps import *

pygame.camera.init()
print(pygame.camera.list_cameras())
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0],(430,530))#,(640,480)
cam.start()
img = cam.get_image()
pygame.image.save(img, "/home/pi/Pictures/hola10.jpg")
img = Image.open("/home/pi/Pictures/hola10.jpg")
mirror(img).show()#cada vez que se muestra la imagen espejar

pygame.camera.quit()

