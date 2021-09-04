import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

ControlPin = [26, 19, 13, 6]

for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

seq = [ [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1]]

for cycle in range(512): # 1evolution = 512cycles (8cycles(=32steps) * 64(gear reduction))
    for halfstep in range(8): # 1cycle = 8halfsteps
        for pin in range(4):
            GPIO.output(ControlPin[pin], seq[halfstep][pin])
        sleep(0.001)
        
GPIO.cleanup()