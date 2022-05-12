import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BOARD)

#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)	
GPIO.setup(18, GPIO.IN)	

#GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN)

#GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN)

ip = "192.168.1.83"

acceso1 = False
spento1 = False

acceso2 = False
spento2 = False

acceso3 = False
spento3 = False


while True:
	
	if GPIO.input(18) == GPIO.HIGH:
		#os.system ("curl https://c05d-176-245-5-112.eu.ngrok.io/cgi-bin/accendo1.py")
		os.system ("curl http://"+ ip +":9000/cgi-bin/accendo1.py")
		if acceso1 == False:
			print('accendo1') 
			acceso1 = True
			spento1 = False
		#time.sleep(0.3)
	
	if GPIO.input(18) == GPIO.LOW:
		if spento1 == False:
			os.system ("curl http://"+ ip +":9000/cgi-bin/spengo1.py")
			print('spengo1')
			spento1 = True
			acceso1 = False
			
	if GPIO.input(22) == GPIO.HIGH:
		#os.system ("curl https://c05d-176-245-5-112.eu.ngrok.io/cgi-bin/accendo2.py")
		os.system ("curl http://" + ip +":9000/cgi-bin/accendo2.py")
		if acceso2 == False:
			print('accendo2') 
			acceso2 = True
			spento2 = False
		#time.sleep(0.3)
	
	if GPIO.input(22) == GPIO.LOW:
		if spento2 == False:
			os.system ("curl http://" + ip + ":9000/cgi-bin/spengo2.py")
			print('spengo2')
			spento2 = True
			acceso2 = False
			
	if GPIO.input(12) == GPIO.HIGH:
		#os.system ("curl https://c05d-176-245-5-112.eu.ngrok.io/cgi-bin/accendo3.py")
		os.system ("curl http://" + ip + ":9000/cgi-bin/accendo3.py")
		if acceso3 == False:
			print('accendo3') 
			acceso3 = True
			spento3 = False
		#time.sleep(0.3)
	
	if GPIO.input(12) == GPIO.LOW:
		if spento3 == False:
			os.system ("curl http://" + ip + ":9000/cgi-bin/spengo3.py")
			print('spengo3')
			spento3 = True
			acceso3 = False
			
