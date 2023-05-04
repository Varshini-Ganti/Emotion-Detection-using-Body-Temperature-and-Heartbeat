import serial
import time
import os
import glob
from urllib.request import urlopen


ser = serial.Serial('/dev/ttyUSB0', 9600) # Replace ttyACM0 with the serial port of the Arduino
ser.flushInput()

myAPI_key = "05UF2XSTQYIUKNP4"  #your Write API key
baseURL = ("https://api.thingspeak.com/update?api_key=%s" %myAPI_key)

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = ser_bytes.decode('utf-8').rstrip()
        print(decoded_bytes)
        conn = urlopen(baseURL + "&field2=%s" %decoded_bytes) #print data entry
        conn.close() 
    except:
        print("Keyboard Interrupt")
        break
