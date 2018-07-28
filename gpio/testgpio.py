import RPi.GPIO as GPIO
import time

pin1Motor1 = 16
pin2Motor1 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin1Motor1, GPIO.OUT)
GPIO.setup(pin2Motor1, GPIO.OUT)

print('1 1')
GPIO.output(pin1Motor1, GPIO.HIGH)
GPIO.output(pin2Motor1, GPIO.HIGH)
time.sleep(2)

print('1 0') # forward
GPIO.output(pin1Motor1, GPIO.HIGH)
GPIO.output(pin2Motor1, GPIO.LOW)
time.sleep(2)

print('0 1') # backward
GPIO.output(pin1Motor1, GPIO.LOW)
GPIO.output(pin2Motor1, GPIO.HIGH)
time.sleep(2)

print('0 0')
GPIO.output(pin1Motor1, GPIO.LOW)
GPIO.output(pin2Motor1, GPIO.LOW)
time.sleep(2)

GPIO.cleanup()
