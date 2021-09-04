import RPi.GPIO as GPIO
from time import sleep, time

SPEED_OF_SOUND = 340

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
NOISE_FILTERING = 10

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO, GPIO.IN)



print ("Starting Measurement...")


seq = [0 for i in range(NOISE_FILTERING)]

while True:
    sleep(0.1)  
    
    for i in range(NOISE_FILTERING):
        GPIO.output(TRIG, 1)
        sleep(0.00001)
        GPIO.output(TRIG, 0)

        while GPIO.input(ECHO) == 0:
            pass
        start = time()

        while GPIO.input(ECHO) == 1:
            pass
        stop = time()

        distance = ((stop - start) * SPEED_OF_SOUND / 2)
        seq[i] = distance
        seq.sort()
        sleep(0.01)
        
    print (seq[-3]*100, '[cm]')
    

GPIO.cleanup()