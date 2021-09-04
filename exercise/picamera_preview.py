from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time

channel = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

GPIO.output(23, GPIO.HIGH)
    
camera = PiCamera()

camera.resolution = (960, 540)
camera.start_preview(fullscreen=False, window=(100,200,960,540))
sleep(30)
camera.stop_preview()
