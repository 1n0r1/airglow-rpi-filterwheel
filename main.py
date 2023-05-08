import serial
from time import sleep
from filterwheel import FilterWheel
import logging
import time
from datetime import datetime

logging.basicConfig(filename='/home/airglow/airglow-rpi-filterwheel/logs/' + datetime.now().strftime('_%Y%m%d_%H%M%S.log'), 
                    format='%(asctime)s %(message)s', 
                    encoding='utf-8', 
                    level=logging.DEBUG)
                    
logging.info('Listener start')
print("Listener start")
ser = serial.Serial(
    port="/dev/serial0", 
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=300
) 


fw = FilterWheel()

while 1:
    x = ser.readline()
    req = x.decode()
    logging.info('Read ' + str(x))

    if req == "home\n":
        logging.info('Homing')
        
        if fw.pos in [0,fw.filter0_pos]: #get away from sensor if you are already there
            fw.goto(fw.filter1_pos)
        fw.home()

        ser.write("homed\n".encode())

    if req == "go0\n":
        logging.info('Going to pos = 0')
        fw.goto(fw.filter0_pos)
        logging.info('Current pos: 0')
        ser.write("pos0\n".encode())
        
    if req == "go1\n":
        logging.info('Going to pos = 1')
        fw.goto(fw.filter1_pos)
        logging.info('Current pos: 1')
        ser.write("pos1\n".encode())
        
    if req == "go2\n":
        logging.info('Going to pos = 2')
        fw.goto(fw.filter2_pos)
        logging.info('Current pos: 2')
        ser.write("pos2\n".encode())
        
    if req == "go3\n":
        logging.info('Going to pos = 3')
        fw.goto(fw.filter3_pos)
        logging.info('Current pos: 3')
        ser.write("pos3\n".encode())