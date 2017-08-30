YOU NEED TO RUN THIS WITH PYTHON 3
To check what version of python is your default:
> python --version
If it says 2.x, see if python3 is installed:
> python3 --version
Whichever one of those says it's version 3.x, use it to run this. Eg:
> python3 run_everything.py


ssh pi@192.168.0.xxx
L1x4rITPi


look here for python module suggestions:
    https://www.adafruit.com/
    https://www.sparkfun.com/
;


TODO
split py files into what goes on quadcampi, wipi, and radiopi
    cam
        4 camera multiplexer
        compass
    wi
        1 camera
        barometer
        temp x5
        temp + humidity
    radio
        1 camera
        radio
        fancy barometer
        gps
        accelerometer
figure out the camera multiplexer - https://github.com/ivmech/ivport