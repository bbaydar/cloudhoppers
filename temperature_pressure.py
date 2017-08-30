import Adafruit_BMP.BMP085 as BMP085
import time

# Default constructor will pick a default I2C bus.
#
# For the Raspberry Pi this means you should hook up to the only exposed I2C bus
# from the main GPIO header and the library will figure out the bus number based
# on the Pi's revision.
#
# For the Beaglebone Black the library will assume bus 1 by default, which is
# exposed with SCL = P9_19 and SDA = P9_20.
#sensor = BMP085.BMP085()

# Optionally you can override the bus number:
#sensor = BMP085.BMP085(busnum=2)

# You can also optionally change the BMP085 mode to one of BMP085_ULTRALOWPOWER,
# BMP085_STANDARD, BMP085_HIGHRES, or BMP085_ULTRAHIGHRES.  See the BMP085
# datasheet for more details on the meanings of each mode (accuracy and power
# consumption are primarily the differences).  The default mode is STANDARD.
#sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)

""" Fetch temperature and pressure data, and log it to file """

def go(output_file, timestamp_format, poll_interval_seconds):
    sensor = BMP085.BMP085()

    print('temperature_pressure is going')
    with open(output_file, 'w') as temp_pressure_file:
        while True:
            print(
                '{}: {0:0.2f} m, {0:0.2f} *C, {0:0.2f} Pa, {0:0.2f} Pa (sea level)'.format(
                    time.strftime(timestamp_format),
                    sensor.read_altitude(),
                    sensor.read_temperature(),
                    sensor.read_pressure(),
                    sensor.read_sealevel_pressure()
                ),
                file=temp_pressure_file
            )
            time.sleep(poll_interval_seconds)
