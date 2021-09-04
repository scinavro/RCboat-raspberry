# This program will let you test your ESC1 and brushless motor.
# Make sure your battery is not connected if you are going to calibrate it at first.
# Since you are testing your motor, I hope you don't have your propeller attached to it otherwise you are in trouble my friend...?
# This program is made by AGT @instructable.com. DO NOT REPUBLISH THIS PROGRAM... actually the program itself is harmful                                             pssst Its not, its safe.

import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library

ESC1=4  #Connect the ESC1 in this GPIO pin 
ESC2=14

pi = pigpio.pi()
pi.set_servo_pulsewidth(ESC1, 0) 
pi.set_servo_pulsewidth(ESC2, 0) 

max_value = 2000 #change this if your ESC1's max value is different or leave it be
min_value = 700  #change this if your ESC1's min value is different or leave it be
print ("For first time launch, select calibrate")
print ("Type the exact word for the function you want")
print ("calibrate OR manual OR control OR arm OR stop")

def manual_drive(): #You will use this function to program your ESC1 if required
    print ("You have selected manual option so give a value between 0 and you max value")
    while True:
        inp = input()
        if inp == "stop":
            stop()
            break
        elif inp == "control": 
            control()
            break
        elif inp == "arm":
            arm()
            break	
        else:
            pi.set_servo_pulsewidth(ESC1,inp)
            pi.set_servo_pulsewidth(ESC2,inp)
                
def calibrate():   #This is the auto calibration procedure of a normal ESC1
    pi.set_servo_pulsewidth(ESC1, 0)
    pi.set_servo_pulsewidth(ESC2, 0)
    print("Disconnect the battery and press Enter")
    inp = input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC1, max_value)
        pi.set_servo_pulsewidth(ESC2, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = input()
        if inp == '':            
            pi.set_servo_pulsewidth(ESC1, min_value)
            pi.set_servo_pulsewidth(ESC2, min_value)
            print ("Wierd eh! Special tone")
            time.sleep(7)
            print ("Wait for it ....")
            time.sleep (5)
            print ("Im working on it, DONT WORRY JUST WAIT.....")
            pi.set_servo_pulsewidth(ESC1, 0)
            pi.set_servo_pulsewidth(ESC2, 0)
            time.sleep(2)
            print ("Arming ESC now...")
            pi.set_servo_pulsewidth(ESC1, min_value)
            pi.set_servo_pulsewidth(ESC2, min_value)
            time.sleep(1)
            print ("See.... uhhhhh")
            control() # You can change this to any other function you want
            
def control(): 
    print ("I'm Starting the motor, I hope its calibrated and armed, if not restart by giving 'x'")
    time.sleep(1)
    speed = 700    # change your speed if you want to.... it should be between 700 - 2000
    print ("Controls - a/h to decrease speed & d/k to increase speed OR q/y to decrease a lot of speed & e/i to increase a lot of speed")
    while True:
        pi.set_servo_pulsewidth(ESC1, speed1)
        pi.set_servo_pulsewidth(ESC2, speed2)
        inp = input()
        
        if inp == "q":
            speed1 -= 100    # decrementing the speed like hell
            print ("speed = %d" % speed1)
        elif inp == "e":    
            speed1 += 100    # incrementing the speed like hell
            print ("speed = %d" % speed1)
        elif inp == "d":
            speed1 += 10     # incrementing the speed 
            print ("speed = %d" % speed1)
        elif inp == "a":
            speed1 -= 10     # decrementing the speed
            print ("speed = %d" % speed1)
        elif inp == "y":
            speed2 -= 100    # decrementing the speed like hell
            print ("speed = %d" % speed2)
        elif inp == "i":    
            speed2 += 100    # incrementing the speed like hell
            print ("speed = %d" % speed2)
        elif inp == "k":
            speed2 += 10     # incrementing the speed 
            print ("speed = %d" % speed2)
        elif inp == "h":
            speed2 -= 10     # decrementing the speed
            print ("speed = %d" % speed2)
        elif inp == "stop":
            stop()          #going for the stop function
            break
        elif inp == "manual":
            manual_drive()
            break
        elif inp == "arm":
            arm()
            break	
        else:
            print ("WHAT DID I SAID!! Press a,q,d or e")
            
def arm(): #This is the arming procedure of an ESC1 
    print ("Connect the battery and press Enter")
    inp = input()    
    if inp == '':
        pi.set_servo_pulsewidth(ESC1, 0)
        pi.set_servo_pulsewidth(ESC2, 0)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC1, max_value)
        pi.set_servo_pulsewidth(ESC2, max_value)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC1, min_value)
        pi.set_servo_pulsewidth(ESC2, min_value)
        time.sleep(1)
        control() 
        
def stop(): #This will stop every action your Pi is performing for ESC1 ofcourse.
    pi.set_servo_pulsewidth(ESC1, 0)
    pi.set_servo_pulsewidth(ESC2, 0)
    pi.stop()

#This is the start of the program actually, to start the function it needs to be initialized before calling... stupid python.    
inp = input()
if inp == "manual":
    manual_drive()
elif inp == "calibrate":
    calibrate()
elif inp == "arm":
    arm()
elif inp == "control":
    control()
elif inp == "stop":
    stop()
else :
    print ("Thank You for not following the things I'm saying... now you gotta restart the program STUPID!!")