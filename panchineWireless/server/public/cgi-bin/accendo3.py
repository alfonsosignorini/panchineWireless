#!/usr/bin/env python3
#f = open("./accendo3", "w")
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,GPIO.HIGH)
#GPIO.cleanup()
