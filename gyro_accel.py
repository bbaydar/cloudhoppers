import time
import mpu6050

""" Reads gyroscope and accelerometer data, and prints it all to log. """

def go(output_file, timestamp_format, poll_interval_seconds):
    mpu = MPU6050(0x68)
    
    print('gyro_accel is going')
    with open(output_file, 'w') as gyro_accel_log:
        while True:
            timestamp = time.strftime(timestamp_format)
            accel_data = mpu.get_accel_data()
            gyro_data = mpu.get_gyro_data()
            
            print('{}: Accelerometer x: {}, y: {}, z: {}'.format(timestamp, accel_data['x'], accel_data['y'], accel_data['z']), file=gyro_accel_log)
            print('{}: Gyroscope x: {}, y: {}, z: {}'.format(timestamp, gyro_data['x'], gyro_data['y'], gyro_data['z']), file=gyro_accel_log)
            
            sleep(poll_interval_seconds)
