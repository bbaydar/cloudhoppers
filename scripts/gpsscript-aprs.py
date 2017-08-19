import gps
import smbus
import time
import aprs.util as aprs

#frame = aprs.create_location_frame('ABC123', '123', '123', 0, 0, 0, '', '');
#print(frame)

bus = smbus.SMBus(1)
TRANSMITTER_ADDRESS = 0x04
 
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

gps_file = open('/var/log/spaceteam/gps-log', 'w')
activity_log_file = open('/var/log/spaceteam/gps-activity-log', 'w')

current_lat = None
current_long = None

def logCoordsDummy():
    global current_lat
    global current_long

    current_lat = 12.345678
    current_long = -34.56789

def logCoords(gps_file, session):

	global current_lat
	global current_long
	try:
        	report = session.next()
                # Wait for a 'TPV' report and display the current time
                # To see all report data, uncomment the line below
        	if report['class'] == 'TPV':
            		if hasattr(report, 'time'):
                		timestamp = str(report.time)
                		long = report.lon
                		lat = report.lat
                		#print(time.strftime("%c") + ', long:' + long + ', lat:' + lat)
               			gps_file.write(time.strftime("%c") + ', long:' + str(long) + ', lat:' + str(lat) + "\n")
				current_lat = lat
				current_long = long
    	except KeyError:
                pass
    	except KeyboardInterrupt:
                pass
	except StopIteration:
                session = None
                print "GPSD has terminated"

def sendAPRS(lat, long, bus, address):
	if(current_lat is not None):
		aprs_lat = '{:.2f}N'.format(abs(lat))
		aprs_long = '{:.2f}W'.format(abs(long))
		aprs_frame = aprs_lat + aprs_long
		aprs_frame = aprs_lat
		
		print(aprs_frame)
		print(lat)
		print(long)
		
		aprs_lat_bytearray = list(bytearray(aprs_lat))
		aprs_long_bytearray = list(bytearray(aprs_long))
		print(aprs_lat_bytearray)
		print(aprs_long_bytearray)
		
		try:
			bus.write_i2c_block_data(address, 33, aprs_lat_bytearray)
			bus.write_i2c_block_data(address, 47, aprs_long_bytearray)
		except IOError as e:
			print('error sending i2c data')
			print(e)
	else:
		print('lat/long not updated')
		activity_log_file.write(time.strftime('%c') + 'latitude was not set for sending aprs data')

while True:
    
    logCoords(gps_file, session)
    #logCoordsDummy()
    sendAPRS(current_lat, current_long, bus, TRANSMITTER_ADDRESS)
    time.sleep(10)
