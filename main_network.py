import serial
import logging
import time

from flask import Flask
from datetime import datetime
from time import sleep

from filterwheel import FilterWheel

logging.basicConfig(filename='/home/airglow/airglow/airglow-rpi-filterwheel/logs/' + datetime.now().strftime('_%Y%m%d_%H%M%S.log'), 
                    format='%(asctime)s %(message)s', 
                    encoding='utf-8', 
                    level=logging.DEBUG)

fw = FilterWheel()




app = Flask(__name__)

@app.route('/')
def index():
    return 'running'
  
@app.route('/home')
def home():
    logging.info('Homing') 
    if fw.pos in [0,fw.filter0_pos]: #get away from sensor if you are already there
        fw.goto(fw.filter1_pos)
    fw.home()
    logging.info('Homed')
    return 'homed'

@app.route('/go/<pos>')
def go(pos):
    if pos == "0":
        logging.info('Going to pos = 0')
        fw.goto(fw.filter0_pos)
        logging.info('Current pos: 0')
        return 'pos0'
    if pos == "1":
        logging.info('Going to pos = 1')
        fw.goto(fw.filter1_pos)
        logging.info('Current pos: 1')
        return 'pos1'
    if pos == "2":
        logging.info('Going to pos = 2')
        fw.goto(fw.filter2_pos)
        logging.info('Current pos: 2')
        return 'pos2'
    if pos == "3":
        logging.info('Going to pos = 3')
        fw.goto(fw.filter3_pos)
        logging.info('Current pos: 3')
        return 'pos3'
    return 'invalid'

if __name__ == '__main__':
    logging.info('Listener start')
    print("Listener start")
    app.run(debug=True, port=8080, host='0.0.0.0')
