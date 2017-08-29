import gps
import smbus
import time
import aprs.util as aprs

""" Fetch GPS data, log it to file, and send it to the APRS module """

# transmitter_address = 0x04
# aprs_host = 'localhost'
# aprs_port = '2947'
# poll_interval_seconds = 10
# output_file = '/var/log/spaceteam/gps-log'
# aprs_bus_address = 1
# timestamp_format = '%Y-%m-%d-%H-%M-%S'


def go(transmitter_address, aprs_host, aprs_port, poll_interval_seconds, output_file, aprs_bus_address, timestamp_format):
    aprs_bus = smbus.SMBus(aprs_bus_address)

    # listen to the gps module
    session = gps.gps(aprs_host, aprs_port)
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    with open(output_file, 'w') as gps_log:
        while True:
            # get crurent GPS data
            report = session.next()
            long = report.long
            lat = report.lat
            timestamp = time.strftime(timestamp_format)
            # log GPS data to file
            print('{}: long: {}, lat: {}'.format(timestamp, long, lat), file=gps_log)
            
            # format GPS data for APRS transmission
            aprs_lat = '{:.2f}N'.format(abs(lat))
            aprs_long = '{:.2f}W'.format(abs(long))
            aprs_lat_bytearray = list(bytearray(aprs_lat))
            aprs_long_bytearray = list(bytearray(aprs_long))
            
            try:
                # send APRS-formatted GPS data to APRS module
                # 33 = ?
                # 47 = ?
                aprs_bus.write_i2c_block_data(transmitter_address, 33, aprs_lat_bytearray)
                aprs_bus.write_i2c_block_data(transmitter_address, 47, aprs_long_bytearray)
            except IOError as e:
                print('error sending i2c data')
                print(e)
            
            time.sleep(poll_interval_seconds)
