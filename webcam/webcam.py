#import 

import cv2
import sys

faceCascade = cv2.CascadeClassifier('/home/pi/work/camera/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')
upperBodyCascade = cv2.CascadeClassifier('/home/pi/work/camera/opencv-3.1.0/data/haarcascades/haarcascade_upperbody.xml')

video_capture = cv2.VideoCapture(0)
video_capture.set(3, 320)
video_capture.set(4, 240)
#video_capture.set(1, -8.0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#    upperBodys = upperBodyCascade.detectMultiScale(
#        gray
#        )

    # Draw a rectangle around the faces
#    for (x, y, w, h) in upperBodys:
#        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#        faces = faceCascade.detectMultiScale(
#                gray,
#                scaleFactor=1.1,
#                minNeighbors=5,
#                minSize=(30, 30),
#                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
#            )
#        for (x, y, w, h) in faces:
#            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

