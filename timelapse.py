from time import sleep
from picamera import PiCamera

""" Snap periodic pictures """

filename_template = './pics/img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'
camera_interval_seconds = 5

camera = PiCamera()
camera.resolution = (3280, 2464)
camera.start_preview()

sleep(2) # give the camera a moment to set its light levels
for filename in camera.capture_continuous(filename_template):
    print('Captured %s' % filename)
    sleep(camera_interval_seconds)
