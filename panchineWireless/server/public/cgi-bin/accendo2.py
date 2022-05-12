#!/usr/bin/env python3
#f = open("./accendo2", "w")
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT)
GPIO.output(24,GPIO.HIGH)
#GPIO.cleanup()
