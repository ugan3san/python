#!/usr/bin/python3
#Message Traffic Stats Logging System

import time
import threading
from datetime import datetime
import random
import sys
import os


class Tsls:

    # class attribute
    recvc: int = 0
    recvf: int = 0
    sentc: int = 0
    sentf: int = 0
    tintl: int = 10
    exefile = os.path.basename(sys.argv[0])
    exefile = os.path.splitext(exefile)[0]
    logfile = "/tmp/np-"+exefile+".log"
    lock = threading.Lock()

    def thread_func(self,):
        while True:
            dt = datetime.fromtimestamp(int(time.time()))
            if(self.recvc > 0):
                with open(self.logfile, "a+") as f:
                    st = str(datetime.fromtimestamp(int(time.time())))
                    st = st+": received "+f'{self.recvf:,}'+" messages of"
                    st = st+" "+f'{self.recvc:,}'+" total bytes\n"
                    f.write(st)
                self.lock.acquire()
                self.recvc = 0
                self.recvf = 0
                self.lock.release()
            if(self.sentc > 0):
                with open(self.logfile, "a+") as f:
                    st = str(datetime.fromtimestamp(int(time.time())))
                    st = st+": transmitted "+f'{self.sentf:,}'+" messages of"
                    st = st+" "+f'{self.sentc:,}'+" total bytes\n"
                    f.write(st)
                self.lock.acquire()
                self.sentc = 0
                self.sentf = 0
                self.lock.release()
            time.sleep(int(self.tintl))

    def __init__(self):
        with open(self.logfile, "a+") as f:
            dt = datetime.fromtimestamp(int(time.time()))
            f.write(str(dt)+": npl started\n")
        x = threading.Thread(target=self.thread_func, args=(), daemon=True)
        x.start()

    def recv(self, size):
        self.recvc += size
        self.recvf += 1

    def sent(self, size):
        self.sentc += size
        self.sentf += 1

    def setlocation(self, dir, tag):
        mm = datetime.now().strftime("%b").lower()
        yy = datetime.now().strftime("%Y")
        self.logfile = dir+"np-"+self.exefile+"-"+tag+"-"+mm+"-"+yy+".log"
        print(self.logfile)

    def setinterval(self, time):
        self.tintl = time


if __name__ == "__main__":
    """
    Entrypoint.
    """

    # channel x
    x = Tsls()
    x.setinterval(10)
    # x.setlocation("/home/ganesanu/log/", "stomp-receive")
    x.setlocation("/tmp/", "stomp-receive")

    # channel y
    y = Tsls()
    y.setinterval(10)
    # y.setlocation("/home/ganesanu/log/", "stomp-transmit")
    y.setlocation("/tmp/", "stomp-transmit")

    dt = datetime.fromtimestamp(int(time.time()))
    print("Date and time is:", dt)
    while True:
        # print("test")
        x.recv(random.randrange(1000, 10000))   # random bytes received
        y.sent(random.randrange(1000, 10000))   # random bytes transmitted
        time.sleep(random.randrange(1, 5))
