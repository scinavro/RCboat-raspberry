import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setwarnings(False)

pwm = GPIO.PWM(buzzer, 100) #(channel, frequency)

pwm.start(100) #duty cycle(0~100)
time.sleep(1)

pwm.stop()
GPIO.cleanup