from time import sleep
from picamera import PiCamera

""" Snap periodic pictures """

def go(filename_template, interval_seconds, resolution, prep_time_seconds):
    camera = PiCamera()
    camera.resolution = resolution
    camera.start_preview()

    print('pictures is going')
    sleep(prep_time_seconds) # give the camera a moment to set its light levels
    for filename in camera.capture_continuous(filename_template):
        print('Captured {}'.format(filename))
        sleep(interval_seconds)
