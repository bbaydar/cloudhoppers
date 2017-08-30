import hmc5883l
import time

""" Fetch compass heading data, and prints it to log. """

def go(gauss_setting, declination_setting, output_file, poll_interval_seconds, timestamp_format):
    # http://magnetic-declination.com/Great%20Britain%20(UK)/Harrogate#
    compass = hmc5883l(gauss = gauss_setting, declination = declination_setting)
    
    print('compass is going')
    with open(output_file, 'w') as compass_log:
        while True:
            timestamp = time.strftime(timestamp_format)
            degrees = compass.degrees(compass.heading())
            print('{}: {}'.format(timestamp, degrees), file=compass_log)
            time.sleep(poll_interval_seconds)
