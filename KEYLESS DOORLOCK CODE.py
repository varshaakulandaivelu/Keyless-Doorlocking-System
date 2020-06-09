import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)
print "DOOR OPEN"
GPIO.output(16,GPIO.HIGH)
time.sleep(10)
print "DOOR CLOSE"
GPIO.output(16,GPIO.LOW)
