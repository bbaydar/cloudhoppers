#!/bin/bash
# https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md
# "This script will take a picture and name the file with a timestamp"

DATE=$(date +"%Y-%m-%d_%H%M%S")

# vf = vertical flip. hf = horizontal flip. combined = rotate image 180 degrees. for when the camera is upside-down
raspistill -vf -hf -o /home/pi/camera/$DATE.jpg
