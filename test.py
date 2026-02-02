#!/bin/usr/python

import sys
import platform
from datetime import datetime
import numpy as np
import subprocess as proc

# basic details.
dt = datetime.now()
d = dt.strftime("%a, %d-%b-%y %H:%M.%S")

pyver = str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro)
os = platform.system()
ver = platform.release()

print("\nThe current date/time is " + d)
print("Using Python " + pyver + "...")
print("Running on " + os + " " + ver)

# Read from file.
print("\nReading from file...\n")
line = None

try:
    #fil = open("py.txt", "r")

     # Fix for UTF-8
     # source: https://stackoverflow.com/questions/491921/unicode-utf-8-reading-and-writing-to-files-in-python

    fil = open("py.txt", mode="r", encoding="utf-8")
    line = fil.readline()
    
    while (line != ""):
        print("debug: " + line, end='')
        line = fil.readline()
    fil.close()
except Exception as e:
    print("Error: " + str(e))
finally:
    fil.close()

# Test array.
a = np.array(["hi", "hola", "hej"])
#a[0] = "hi"
#a[1] = "hola"
#a[2] = "hej"

print("\narray element 2 = " + a[1] + "\n")

for ae in a:
    print("arr: " + ae)

#a[3] = "hallo"
a = np.append(a, "hallo")
sz = np.size(a)
print("\narray size = " + str(sz))
print("")

# https://stackoverflow.com/questions/7332841/add-single-element-to-array-in-numpy

#for s in range(0, sz-1):
for s in range(0, sz):
    print("larger arr: " + a[s])

# OJO: the range() starts at 0 by default, increments by 1, and stops BEFORE the specified number.
# Thus, in lieu of the usual size - 1 approach, you simply specify the actual size!

# Test command.
#cmd = "scurl -V"
print("")
proc.run(["scurl", "-V"])

op = proc.run(["scurl", "-V"], stdout=proc.PIPE)
#tmp = proc.run(["scurl", "-V"], shell=True)
#op = tmp.stdout

print("\noutput:")
#print("\noutput: " + str(op))
#print(op)
op = str(op)
#op2 = op.split(',')
op = op.replace("\\r\\n", "\n")
#for line in op.split('\n'):
for line in op.split(','):
    if ( line.startswith(" stdout") ):
        print(line[10:-2])
    #print(line)

# Test hash
dict = {
    "first": "Bernard",
    "last": "Simmons",
    "id": 123,
    "title": "Engineer"
}

print("\nPrinting employee information...")
print("Name: " + dict["first"] + " " + dict["last"])
print("Employee ID: " + str(dict["id"]))
print("Title: " + dict["title"])
print("")
print("Done\n")