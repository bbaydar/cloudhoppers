from time import sleep
from picamera import PiCamera
from datetime import datetime, timedelta

camera = PiCamera()
camera.resolution = (3280, 2464)
camera.start_preview()

sleep(2)
for filename in camera.capture_continuous('./pics/img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
    print('Captured %s' % filename)
    sleep(5)
