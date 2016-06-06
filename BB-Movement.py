#Import Libraries
import RPi.GPIO as GPIO
import time
import picamera
#import time
#import datetime
#import os

#Configure GPIO #19 for LISIPAROI
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT) 

GPIO.output(19, GPIO.HIGH) # Turn on LEDs

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(5) #sleep 5 seconds
    camera.capture('/home/pi/Documents/BirdBox/Motion/image.jpg') #Take Picture
    camera.stop_preview() 
#	os.rename("/home/pi/Documents/BirdBox/Motion/image.jpg", time.strftime("/home/pi/Documents/BirdBox/Motion/BBM_%Y%m%d%H%M.jpg"))

GPIO.output(19, GPIO.LOW) #Turn off LEDs
