import gps_aprs

# global
timestamp_format = '%Y-%m-%d-%H-%M-%S'

# gps_aprs
gps_aprs_transmitter_address = 0x04
gps_aprs_host = 'localhost'
gps_aprs_port = '2947'
gps_aprs_poll_interval_seconds = 10
gps_aprs_output_file = '/var/log/spaceteam/gps-log'
gps_aprs_bus_address = 1

# hmc5883l
hmc5883l_gauss = 4.7
hmc5883l_declination = (-2, 5)
hmc5883l_output_file = '/var/log/spaceteam/compass-log'
hmc5883l_poll_interval_seconds = 10

gps_aprs.go(gps_aprs_transmitter_address, gps_aprs_host, gps_aprs_port, gps_aprs_poll_interval_seconds, gps_aprs_output_file, gps_aprs_bus_address, timestamp_format)

