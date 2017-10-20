import RPi.GPIO as GPIO
import time
import pyautogui

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)#izquierda
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)#abajo
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)#arriba
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)#derecha
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)#start
arriba=False
abajo=False
derecha=False
izquierda=False
start=False

while True:


    input_state = GPIO.input(26)
    if input_state == False:
        if izquierda==False:
            print("se presiono izquierda")
            pyautogui.press('left')
            izquierda=True
    else:
       izquierda=False

    input_state = GPIO.input(13)
    if input_state == False:
        if abajo == False:
            print("se presiono abajo")
            pyautogui.press('down')
            abajo=True
    else:
        abajo=False

    input_state = GPIO.input(6)
    if input_state == False:
        if arriba==False:
            print("se presiono arriba")
            pyautogui.press('up')
            arriba=True
    else:
        arriba=False

    input_state = GPIO.input(5)
    if input_state == False:
        if derecha==False:
            print("se presiono derecha")
            pyautogui.press('right')
            derecha=True
    else:
        derecha=False

    input_state = GPIO.input(16)
    if input_state == False:
        if start==False:
            print("se presiono start")
            pyautogui.press('tab')
            start=True
    else:
        start=False

    time.sleep(0.2)



