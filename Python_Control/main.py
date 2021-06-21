"""
This script aims to control the PWM port of an Arduino board.

Author: Vincent STRAGIER

Install on Windows: py -3.8 -m pip install -r requirements.txt
List ports on Windows: py -3.8 -m serial.tools.list_ports
"""

from time import sleep

import serial
import serial.tools.list_ports


DELAY = 0.1
PORT_INDEX = 0


def main():
    # List ports
    ports = [comport.device for comport in serial.tools.list_ports.comports()]
    n_ports = len(ports)
    print('Ports list:', ports)

    if n_ports:
        # Open port
        with serial.Serial(ports[PORT_INDEX], 115200) as ser:
            print(ser.readline().decode('UTF8'), end='')

            # Increase and decrease a value from 0 to 255
            while 1:
                for i in range(0, 256):
                    ser.write(str(i).encode('UTF8'))
                    print(ser.readline().decode('UTF8'), end='')
                    sleep(DELAY)

                for i in range(1, 255):
                    ser.write(str(255 - i).encode('UTF8'))
                    print(ser.readline().decode('UTF8'), end='')
                    sleep(DELAY)


if __name__ == '__main__':
    main()
