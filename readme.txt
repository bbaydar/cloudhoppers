YOU NEED TO RUN THIS WITH PYTHON 3
> python3 run_everything.py

gpsscript-aprs.py: loops every 10 seconds to read gps data and write to /var/log/spaceteam/gps-log, then sends gps data to APRS module via smbus i2c
timelapse.py: loops every 5 seconds to take pictures and save to ./pics/
temperature-pressure.py: loops every 10 seconds to read temperatures and pressures and write to /var/log/spaceteam/temp-pressure-log
hmc5883l.py: loops every 10 seconds to read compass heading data and write to /var/log/spaceteam/compass-log

TODO
write a script to run just before launching that will start everything
put all the args into that script? log name and location, poll interval, ...

ssh pi@192.168.0.114
L1x4rITPi


look here for python module suggestions:
    https://www.adafruit.com/
    https://www.sparkfun.com/
;
