import gps_aprs
import compass
import pictures
import temperature_pressure
import gyro_accel

""" Central location for
    a) setting values like log file locations and names, run intervals, and camera resolution,
    b) starting all of the modules using the set values
"""

# general
timestamp_format = '%Y-%m-%d-%H-%M-%S'
poll_interval_seconds = 10

# gps and aprs
gps_aprs_transmitter_address = 0x04
gps_aprs_host = 'localhost'
gps_aprs_port = '2947'
gps_aprs_output_file = '/var/log/spaceteam/gps_arps.log'
gps_aprs_bus_address = 1

# compass
compass_gauss = 4.7
compass_declination = (-2, 5)
compass_output_file = '/var/log/spaceteam/compass.log'

# pretty pictures
picture_filename_template = './pics/img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'
picture_interval_seconds = 5
picture_camera_resolution = (3280, 2464)
picture_camera_prep_time_seconds = 2

# temperature and pressure
temperature_pressure_output_file = '/var/log/spaceteam/temp_pressure.log'

# gyroscope and accelerometer
gyro_accel_output_file = '/var/log/spaceteam/gyro_accel.log'

# start everything!
gps_aprs.go(gps_aprs_transmitter_address, gps_aprs_host, gps_aprs_port, poll_interval_seconds, gps_aprs_output_file, gps_aprs_bus_address, timestamp_format)
compass.go(compass_gauss, compass_declination, compass_output_file, poll_interval_seconds, timestamp_format)
pictures.go(picture_filename_template, picture_interval_seconds, picture_camera_resolution, picture_camera_prep_time_seconds)
temperature_pressure.go(temperature_pressure_output_file, timestamp_format, poll_interval_seconds)
gyro_accel.go(gyro_accel_output_file, timestamp_format, poll_interval_seconds)
