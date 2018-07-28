import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BOARD)    # use BOARD to label PINs
IO.setup(12, IO.OUT)    # use PIN 12 as PWM output
p = IO.PWM(12, 50)      # frequency = 50Hz, meaning 1 cycle is 20ms (50Hz)

'''
for SG90 servo, it works under frequency 50Hz,
and the pulse width (duty cycle) decides the position of the servo,
there are also maximum and minimum pulse width

0 degree   = 2.5
180 degree = 12.0
'''
per = (12.5 - 2.5) / 180.0

p.start(0.0)
while 1:
    for angle in range(0, 180, 30):
        dc = (2.5 + angle * per)
        print('Angle: {}, dc: {}'.format(angle, dc))
        p.ChangeDutyCycle(dc)
        time.sleep(1)
    for angle in range(180, 0, -30):
        dc = (2.5 + angle * per)
        print('Angle: {}, dc: {}'.format(angle, dc))
        p.ChangeDutyCycle(dc)
        time.sleep(1)
