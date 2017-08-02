
import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

display = pygame.display.set_mode((640,480), 0)
cam = pygame.camera.Camera("/dev/video0",(640,480))
snapshot = pygame.surface.Surface((640,480), 0, display)
cam.start()
image = cam.get_image()
going = True
while going:
    events = pygame.event.get()
    for e in events:
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            # close the camera safely
            cam.stop()
            going = False

    if cam.query_image():
        snapshot = cam.get_image(snapshot)

        # blit it to the display surface.  simple!
        display.blit(snapshot, (0,0))
        pygame.display.flip()