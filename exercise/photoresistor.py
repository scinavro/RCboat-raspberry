import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)

while True:
    print (GPIO.input(11))
    time.sleep(0.2) 