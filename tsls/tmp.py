#!/usr/bin/python3

from datetime import datetime
import sys
import os

# global vars
recvc = 0
tintl = 10

currentm = datetime.now().strftime("%b")
currenty = datetime.now().strftime("%Y")

print(currentm)
print(currenty)

exefile = os.path.basename(sys.argv[0])
exefile = os.path.splitext(exefile)[0]

logfile = "/home/ganesanu/log/np-"+exefile+"-"+currenty+"-"+currentm+".log"
print(logfile)


