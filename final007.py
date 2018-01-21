#!/usr/bin/python
import  RPi.GPIO as GPIO
import time
import os


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
   inputValue = GPIO.input(18)
   if (inputValue == False):
       print("capturing image ")
       time.sleep(0.2)
       os.system("raspistill -o cam.jpg")
       os.system('tesseract ' + '/home/pi/cam.jpg ' + '/home/pi/Documents/zeiss/data')
       
       print('image to text')
       
       os.system('espeak '+ '-s 140 -f '+'/home/pi/Documents/zeiss/data.txt')

       print('text to speech ')      
       

    
