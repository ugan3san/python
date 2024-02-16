#!/usr/bin/python3

import time
import threading
from datetime import datetime
import sys
import os

import random
from tsls import Tsls

if __name__ == "__main__":

    # channel x
    x = Tsls()
    x.setinterval(10)
    x.setlocation("/home/ganesanu/log/", "stomp-receive")

    # channel y
    y = Tsls()
    y.setinterval(30)
    y.setlocation("/home/ganesanu/log/", "stomp-transmit")

    dt = datetime.fromtimestamp(int(time.time()))
    print("Date and time is:", dt)
    while True:
        # print("test")
        x.recv(random.randrange(1000, 10000))   # random bytes received
        y.sent(random.randrange(1000, 10000))   # random bytes transmitted
        time.sleep(random.randrange(1, 5))
	    # time.sleep(10)
