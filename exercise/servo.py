import RPi.GPIO as GPIO
from time import sleep                                                            

servoPin = 25
SERVO_MAX_DUTY = 20
SERVO_MIN_DUTY = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)

servo = GPIO.PWM(servoPin, 100)
servo.start(0)

def setServoPos(degree):
    if degree > 180:
        degree = 180
    
    duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
    print("Degree: {} to {}(Duty)".format(degree, duty))

    servo.ChangeDutyCycle(duty)

if __name__ == "__main__":
    while True:
        for i in range(4):
            setServoPos((i)*45)
            sleep(1)
        for i in range(4, 0, -1):
            setServoPos((i)*45)
            sleep(1)
    GPIO.cleanup()
