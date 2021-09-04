import RPi.GPIO as GPIO
import time

channel = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

def led_on(pin):
    GPIO.output(pin, GPIO.HIGH)
    
def led_off(pin):
    GPIO.output(pin, GPIO.LOW)
    
if __name__ == '__main__':
    while True:
        GPIO.output(23, GPIO.LOW)
