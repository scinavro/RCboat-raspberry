from gpiozero import LED
from time import sleep

led = LED(4)

while True:
    led.off()
    sleep(0.5)
    