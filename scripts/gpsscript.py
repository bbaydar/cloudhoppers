import gps
import smbus
import time

bus = smbus.SMBus(1)
 
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

gps_file = open('/var/log/spaceteam/gps-log', 'w')


while True:
    try:
    	report = session.next()
		# Wait for a 'TPV' report and display the current time
		# To see all report data, uncomment the line below
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                timestamp = str(report.time)
		long = str(report.lon)
		lat = str(report.lat)
		#print(time.strftime("%c") + ', long:' + long + ', lat:' + lat)
		gps_file.write(time.strftime("%c") + ', long:' + long + ', lat:' + lat + "\n")
	        time.sleep(10)
    except KeyError:
		pass
    except KeyboardInterrupt:
		quit()
    except StopIteration:
		session = None
		print "GPSD has terminated"