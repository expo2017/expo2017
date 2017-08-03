import pygame.camera
import pygame.image

pygame.camera.init()
print(pygame.camera.list_cameras())
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()
img = cam.get_image()
pygame.image.save(img, "/home/alumno/Imágenes/fotopersona/photo.jpg")
pygame.image.save(img, "photo.pdf")
pygame.image.save(img, "photo.bmp")
pygame.image.save(img, "photo.jpg")
pygame.camera.quit()

