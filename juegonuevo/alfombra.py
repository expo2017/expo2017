import RPi.GPIO as GPIO
import time
#import pyautogui

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)#izquierda
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)#abajo
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)#arriba
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)#derecha
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)#start


while True:
    input_state = GPIO.input(26)
    if input_state == False:
        #press('left')
        print("se presiono izquierda")
         #Lo que tengas que hacer
    input_state = GPIO.input(13)
    if input_state == False:
        # press('down')
        print("se presiono abajo")

    input_state = GPIO.input(6)
    if input_state == False:
        # press('up')
        print("se presiono arriba")

    input_state = GPIO.input(5)
    if input_state == False:
        # press('right')
        print("se presiono derecha")
    input_state = GPIO.input(16)
    if input_state == False:
        # press('tab')
        print("se presiono start")

    time.sleep(1.4)



