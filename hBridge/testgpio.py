import RPi.GPIO as GPIO
import time

pin1Motor1 = 16
pin2Motor1 = 18

pin1Motor2 = 13
pin2Motor2 = 15

GPIO.setmode(GPIO.BOARD)
# Motor1 setup
GPIO.setup(pin1Motor1, GPIO.OUT)
GPIO.setup(pin2Motor1, GPIO.OUT)
# Motor2 setup
GPIO.setup(pin1Motor2, GPIO.OUT)
GPIO.setup(pin2Motor2, GPIO.OUT)

print('Foward') # forward
# Motor1 forward
GPIO.output(pin1Motor1, GPIO.HIGH)
GPIO.output(pin2Motor1, GPIO.LOW)
# Motor2 forward
GPIO.output(pin1Motor2, GPIO.HIGH)
GPIO.output(pin2Motor2, GPIO.LOW)
time.sleep(5)

print('Backward') # backward
# Motor1 backward
GPIO.output(pin1Motor1, GPIO.LOW)
GPIO.output(pin2Motor1, GPIO.HIGH)
# Motor2 backward
GPIO.output(pin1Motor2, GPIO.LOW)
GPIO.output(pin2Motor2, GPIO.HIGH)
time.sleep(5)

print('Turn ?') # turn
# Motor1 forward
GPIO.output(pin1Motor1, GPIO.HIGH)
GPIO.output(pin2Motor1, GPIO.LOW)
# Motor2 backward
GPIO.output(pin1Motor2, GPIO.LOW)
GPIO.output(pin2Motor2, GPIO.HIGH)
time.sleep(5)

print('Turn ?') # turn
# Motor1 backward
GPIO.output(pin1Motor1, GPIO.LOW)
GPIO.output(pin2Motor1, GPIO.HIGH)
# Motor2 forward
GPIO.output(pin1Motor2, GPIO.HIGH)
GPIO.output(pin2Motor2, GPIO.LOW)
time.sleep(5)

GPIO.cleanup()
