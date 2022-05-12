#!/usr/bin/env python3
#f = open("./accendo1", "w")
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.HIGH)
#GPIO.cleanup()
