######## Webcam Object Detection Using Tensorflow-trained Classifier #########
#
# Author: Evan Juras
# Date: 10/27/19
# DESC1ription: 
# This program uses a TensorFlow Lite model to perform object detection on a live webcam
# feed. It draws boxes and scores around the objects of interest in each frame from the
# webcam. To improve FPS, the webcam object runs in a separate thread from the main program.
# This script will work with either a Picamera or regular USB webcam.
#
# This code is based off the TensorFlow Lite image classification example at:
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/examples/python/label_image.py
#
# I added my own method of drawing boxes and labels using OpenCV.

# Import packages
import os
import argparse
import cv2
import numpy as np
import sys
import time
from threading import Thread
import importlib.util
import socket
import serial
import pynmea2
#import imutils
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library
import RPi.GPIO as GPIO
from time import sleep                                                           

HOST = '192.168.227.179'
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

LIGHT_SENSOR = 11


channel = 23

ESC_L=4  #Connect the ESC_L in this GPIO pin 
ESC_R=14

servoPin = 25
SERVO_MAX_DUTY = 20
SERVO_MIN_DUTY = 4

max_value = 2000 
min_value = 500

isDetected = False
isTouched = True
increase = True
x_dif = 0
angle = 0
STOP_SPEED = 600
BASE_SPEED = 1100
TURN_SPEED = 1200

pi = pigpio.pi()
pi.set_servo_pulsewidth(ESC_L, 0) 
pi.set_servo_pulsewidth(ESC_R, 0) 

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)
GPIO.setup(channel, GPIO.OUT)

GPIO.setup(LIGHT_SENSOR, GPIO.IN)

servo = GPIO.PWM(servoPin, 100)
servo.start(0)

def remap_range(
    val: float,
    old_min: float,
    old_max: float,
    new_min: float,
    new_max: float,
    saturate: bool = False,
) -> float:
    
    old_span: float = old_max - old_min
    new_span: float = new_max - new_min
    new_val: float = new_min + new_span * (float(val - old_min) / float(old_span))

    # If saturate is true, enforce the new_min and new_max limits
    if saturate:
        if new_min < new_max:
            return clamp(new_val, new_min, new_max)
        else:
            return clamp(new_val, new_max, new_min)

    return new_val

def calibrate():   #This is the auto calibration procedure of a normal ESC_L
    pi.set_servo_pulsewidth(ESC_L, 0)
    pi.set_servo_pulsewidth(ESC_R, 0)
    print("Disconnect the battery and press Enter")
    inp = input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC_L, max_value)
        pi.set_servo_pulsewidth(ESC_R, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = input()
        if inp == '':            
            pi.set_servo_pulsewidth(ESC_L, min_value)
            pi.set_servo_pulsewidth(ESC_R, min_value)
            print ("Wierd eh! Special tone")
            time.sleep(7)
            print ("Wait for it ....")
            time.sleep (5)
            print ("Im working on it, DONT WORRY JUST WAIT.....")
            pi.set_servo_pulsewidth(ESC_L, 0)
            pi.set_servo_pulsewidth(ESC_R, 0)
            time.sleep(2)
            print ("Arming ESC now...")
            pi.set_servo_pulsewidth(ESC_L, min_value)
            pi.set_servo_pulsewidth(ESC_R, min_value)
            time.sleep(1)
            print ("See.... uhhhhh")

def control():
    global angle
    # time.sleep(1)
    speed_L = BASE_SPEED
    speed_R = BASE_SPEED
    
    if (angle > 90):
        speed_L = remap_range(angle, 90, 140, BASE_SPEED, TURN_SPEED)
        print ("speed_L = %d" % speed_L)
        print ("speed_R = %d" % speed_R)
    else:
        speed_R = remap_range(angle, 40, 90, TURN_SPEED, BASE_SPEED)
        print ("speed_L = %d" % speed_L)
        print ("speed_R = %d" % speed_R)
    pi.set_servo_pulsewidth(ESC_L, speed_L)
    pi.set_servo_pulsewidth(ESC_R, speed_R)
    
def stop():
    pi.set_servo_pulsewidth(ESC_L, STOP_SPEED)
    pi.set_servo_pulsewidth(ESC_R, STOP_SPEED)
    print ("speed_L = %d" % speed_L)
    print ("speed_R = %d" % speed_R)

def Servo(degree):
    global angle
    angle = degree
    if angle > 140:
        angle = 140
    elif angle < 40:
        angle = 40
    duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
    servo.ChangeDutyCycle(duty)
    print("Degree: {} to {}(Duty)".format(degree, duty))

# Define VideoStream class to handle streaming of video from webcam in separate processing thread
# Source - Adrian Rosebrock, PyImageSearch: https://www.pyimagesearch.com/2015/12/28/increasing-raspberry-pi-fps-with-python-and-opencv/
class VideoStream:
    """Camera object that controls video streaming from the Picamera"""
    def __init__(self,resolution=(960,540),framerate=30):
        # Initialize the PiCamera and the camera image stream
        self.stream = cv2.VideoCapture(0)
        ret = self.stream.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        ret = self.stream.set(3,resolution[0])
        ret = self.stream.set(4,resolution[1])
            
        # Read first frame from the stream
        (self.grabbed, self.frame) = self.stream.read()

	# Variable to control when the camera is stopped
        self.stopped = False

    def start(self):
	# Start the thread that reads frames from the video stream
        Thread(target=self.update,args=()).start()
        return self

    def update(self):
        # Keep looping indefinitely until the thread is stopped
        while True:
            # If the camera is stopped, stop the thread
            if self.stopped:
                # Close camera resources
                self.stream.release()
                return

            # Otherwise, grab the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
	# Return the most recent frame
        return self.frame

    def stop(self):
	# Indicate that the camera and thread should be stopped
        self.stopped = True
   
    

def recognize():
    global isDetected
    global x_dif
    
    print ("recognize")
# Grab frame from video stream
    frame1 = videostream.read()
    # Acquire frame and resize to expected shape [1xHxWx3]
    frame = frame1.copy()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame_rgb, (width, height))
    input_data = np.expand_dims(frame_resized, axis=0)

    # Normalize pixel values if using a floating model (i.e. if model is non-quantized)
    # if floating_model:
    #     input_data = (np.float32(input_data) - input_mean) / input_std

    # Perform the actual detection by running the model with the image as input
    interpreter.set_tensor(input_details[0]['index'],input_data)
    interpreter.invoke()

    # Retrieve detection results
    boxes = interpreter.get_tensor(output_details[0]['index'])[0] # Bounding box coordinates of detected objects
    classes = interpreter.get_tensor(output_details[1]['index'])[0] # Class index of detected objects
    scores = interpreter.get_tensor(output_details[2]['index'])[0] # Confidence of detected objects
    #num = interpreter.get_tensor(output_details[3]['index'])[0]  # Total number of detected objects (inaccurate and not needed)
    
    noPerson = True
    for i in range(len(scores)):
        if (labels[int(classes[i])]!="person"):
            continue
        
        if ((scores[i] > min_conf_threshold) and (scores[i] <= 1.0)):

            # Get bounding box coordinates and draw box
            # Interpreter can return coordinates that are outside of image dimensions, need to force them to be within image using max() and min()
            # ymin = int(max(1,(boxes[i][0] * imH)))
            xmin = int(max(1,(boxes[i][1] * imW)))
            # ymax = int(min(imH,(boxes[i][2] * imH)))
            xmax = int(min(imW,(boxes[i][3] * imW)))
            
            x = (xmax + xmin) / 2
            x_dif = x - imW/2 
            # print("x:", x)
            # print("imW: ", imW)
            print("X_dif: ", x_dif)
            
            # cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), (10, 255, 0), 2)
            

            # Draw label
            # object_name = labels[int(classes[i])] # Look up object name from "labels" array using class index
            # label = '%s: %d%%' % (object_name, int(scores[i]*100)) # Example: 'person: 72%'
            # labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) # Get font size
            # label_ymin = max(ymin, labelSize[1] + 10) # Make sure not to draw label too close to top of window
            # cv2.rectangle(frame, (xmin, label_ymin-labelSize[1]-10), (xmin+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED) # Draw white box to put label text in
            # cv2.putText(frame, label, (xmin, label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) # Draw label text 
            
            isDetected = True
            print("Person Detected, 'isDetected': ", isDetected)
            noPerson = False
            
    if (noPerson):
        isDetected = False
        print("Person Not Detected, 'isDetected': ", isDetected)
    
    # Draw framerate in corner of frame
    # cv2.putText(frame,'FPS: {0:.2f}'.format(frame_rate_calc),(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)

    # All the results have been drawn on the frame, so it's time to display it.
    # cv2.imshow('Object detector', frame)

def getGPS():
    port="/dev/ttyAMA0"
    ser=serial.Serial(port, baudrate=9600, timeout=0.5)
    byteData=ser.readline()
    strData = byteData.decode('latin_1')

    
    if strData[0:6] == '$GNGGA':
        newmsg=pynmea2.parse(strData)
        lat=newmsg.latitude
        lng=newmsg.longitude
        
        gps = "Latitude = " + str(lat) + "  and  Longitude = " + str(lng) 
        return(gps)

def lightCheck():
    global channel
    if GPIO.input(LIGHT_SENSOR) == 1:
        GPIO.output(channel, GPIO.HIGH)
    else:
        GPIO.output(channel, GPIO.LOW)
        
calibrate()

# Define and parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument('--modeldir', help='Folder the .tflite file is located in',
                    required=True)
parser.add_argument('--graph', help='Name of the .tflite file, if different than detect.tflite',
                    default='detect.tflite')
parser.add_argument('--labels', help='Name of the labelmap file, if different than labelmap.txt',
                    default='labelmap.txt')
parser.add_argument('--threshold', help='Minimum confidence threshold for displaying detected objects',
                    default=0.5)
parser.add_argument('--resolution', help='Desired webcam resolution in WxH. If the webcam does not support the resolution entered, errors may occur.',
                    default='960x540')
parser.add_argument('--edgetpu', help='Use Coral Edge TPU Accelerator to speed up detection',
                    action='store_true')

args = parser.parse_args()

MODEL_NAME = args.modeldir
GRAPH_NAME = args.graph
LABELMAP_NAME = args.labels
min_conf_threshold = float(args.threshold)
resW, resH = args.resolution.split('x')
imW, imH = int(resW), int(resH)
use_TPU = args.edgetpu

# Import TensorFlow libraries
# If tflite_runtime is installed, import interpreter from tflite_runtime, else import from regular tensorflow
# If using Coral Edge TPU, import the load_delegate library
pkg = importlib.util.find_spec('tflite_runtime')
if pkg:
    from tflite_runtime.interpreter import Interpreter
    if use_TPU:
        from tflite_runtime.interpreter import load_delegate
else:
    from tensorflow.lite.python.interpreter import Interpreter
    if use_TPU:
        from tensorflow.lite.python.interpreter import load_delegate

# If using Edge TPU, assign filename for Edge TPU model
if use_TPU:
    # If user has specified the name of the .tflite file, use that name, otherwise use default 'edgetpu.tflite'
    if (GRAPH_NAME == 'detect.tflite'):
        GRAPH_NAME = 'edgetpu.tflite'       

# Get path to current working directory
CWD_PATH = os.getcwd()

# Path to .tflite file, which contains the model that is used for object detection
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,GRAPH_NAME)

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,MODEL_NAME,LABELMAP_NAME)

# Load the label map
with open(PATH_TO_LABELS, 'r') as f:
    labels = [line.strip() for line in f.readlines()]

# Have to do a weird fix for label map if using the COCO "starter model" from
# https://www.tensorflow.org/lite/models/object_detection/overview
# First label is '???', which has to be removed.
if labels[0] == '???':
    del(labels[0])

# Load the Tensorflow Lite model.
# If using Edge TPU, use special load_delegate argument
if use_TPU:
    interpreter = Interpreter(model_path=PATH_TO_CKPT,
                              experimental_delegates=[load_delegate('libedgetpu.so.1.0')])
    print(PATH_TO_CKPT)
else:
    interpreter = Interpreter(model_path=PATH_TO_CKPT)

interpreter.allocate_tensors()


speed_L = STOP_SPEED
speed_R = STOP_SPEED
pi.set_servo_pulsewidth(ESC_L, speed_L)
pi.set_servo_pulsewidth(ESC_R, speed_R)

# Get model details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

floating_model = (input_details[0]['dtype'] == np.float32)

input_mean = 127.5
input_std = 127.5

# Initialize frame rate calculation
# frame_rate_calc = 1
# freq = cv2.getTickFrequency()

# Initialize video stream
videostream = VideoStream(resolution=(imW,imH),framerate=30).start()
time.sleep(1)

#for frame1 in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
while True:
    
    while(not isDetected):
        stop()
        print("=====Surveillance Mode=====")
        
        if (increase):
            angle += 5
        if (angle > 140):
            angle = 140
            increase = False
        if (not increase):
            angle -= 5
        if (angle < 40):
            angle = 45
            increase = True
            
        Servo(angle)
        # Start timer (for calculating frame rate)
        # t1 = cv2.getTickCount()
        recognize()
        lightCheck()
        
        # s.send('isDetected = False')

    data = "isDetected = True Latitude = 36.345  and  Longitude = 176.1231"
    # s.send(data.encode())
            
    while(isDetected):
        print("=====Tracking Mode=====")
        print("x_dif: ", x_dif)
        if(abs(x_dif)>50):
            if (x_dif > 0):
                angle += 5
            else:
                angle -= 5
            print("angle: ", angle)
            Servo(angle)
        else:
            pass
        
        control()    
        recognize()
        
        data = 'isDetected = True'
        s.send(data.encode())
        
    if(isTouched):
        print("====Boat is touched====")
        data1 = 'isTouched = True' 
        s.send(data1.encode())
        # gps = getGPS()
        # s.send(gps)
        data2 = 'Latitude = 36.345  and  Longitude = 176.1231'  
        s.send(data2.encode())

    # Calculate framerate
    # t2 = cv2.getTickCount()
    # time1 = (t2-t1)/freq
    # frame_rate_calc= 1/time1

    # Press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break
    
# Clean up
cv2.destroyAllWindows()
videostream.stop()
