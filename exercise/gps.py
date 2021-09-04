import serial
import pynmea2

while True:
    port="/dev/ttyAMA0"
    ser=serial.Serial(port, baudrate=9600, timeout=0.5)
    byteData=ser.readline()
    strData = byteData.decode('latin_1')

    
    if strData[0:6] == '$GNGGA':
        newmsg=pynmea2.parse(strData)
        lat=newmsg.latitude
        lng=newmsg.longitude
        
        gps = "Latitude = " + str(lat) + "  and  Longitude = " + str(lng) 
        print(gps)