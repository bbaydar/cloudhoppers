import smbus
import time
bus = smbus.SMBus(1)
address1 = 0x69
address2 = 0x1e
address3 = 0x77

def data1():
    d1 = bus.read_byte_data(address1, 1)
    return d1

def data2():
    d2 = bus.read_byte_data(address2, 1)
    return d2

def data3():
    d3 = bus.read_byte_data(address3, 1)

while True:
    print data1()
    print data2()
	print data3()
    print "\n"
    time.sleep(1)

