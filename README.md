# RaspberryPi3
To summarize all I learnt from playing with my RaspberryPi3
The following bulletins list all my experience on RaspberryPi3.

## Servo control SG90
A python script to turn SG90 servo, using PWM.

## Surveillance Camera
A python script to use WebCam (or other cameras) to detect faces.
(Need some configuration on the face detection part.)

## GPS
On Raspbian OS, I successfully connected GPS module to RaspberryPi3.
Refer to the 2 pics in ./GPS for detail on connection and terminal commands.

## hBridge
Python script to control 4 motor vehicle.

## webcam
Python script to use webcam on Raspberry Pi
- pi_surveillance_web.py, open a window to show webcam input. Also detect the moving pixels on a frame, and detect faces in the those pixels (need OpenCV support).
- webcam.py, simple open a window to show webcam input.