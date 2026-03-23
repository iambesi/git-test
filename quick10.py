#!/usr/bin/python

# To-do:
# Basics: date/time, py ver, os ver
# argument passing
# read from file
# conditional
# arrays
# for loop
# run command
# dictionary (hash)
# function

import sys
import platform
import argparse
import numpy as np
import subprocess as sp
from datetime import datetime

dt = datetime.now()
d = dt.strftime("%a, %d-%b-%y %H:%M:%S")
pyver = str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro)
osver = platform.system() + " " + platform.release()

print("\nToday's date is " + d)
print("Python version: " + pyver)
print("OS version: " + osver)

print("")

# arguments.

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename")
parser.add_argument("-m", "--message")
args = parser.parse_args()

if ( args.message ):
   print("Your message is: " + args.message)
else:
   print("No message was entered.")

# file reading.

if args.filename:
   print("\nAttempting to read from file '" + args.filename + "'...\n")

   line = None
   fil = None

   try:
      fil = open(args.filename, "r", encoding='utf8')

      while( line != "" ):
         line = fil.readline()

         if ( line != "" ): print("file: " + line, end='')
   except Exception as e:
      print("Error: " + str(e))
   finally:
      if fil: fil.close()
else:
   print("Error: no file name was specified!")

# arrays.

print("\nTesting arrays...\n")

arr = np.array(["hello", "hej", "oi"])

for a in arr:
   print("foreach: " + a)

print("")

sz = np.size(arr)
for i in range(0, sz):
   print("range: " + arr[i])

print("")
arr = np.append(arr, "\u00a1hola!")
for b in arr:
   print("append: " + b)

print("\nTesting hashes...\n")

emp = {
   "id": 12,
   "name": "Bernard Simmons",
   "title": "Engineer"
}

print("Employee ID: " + str(emp["id"]))
print("Employee name: " + emp["name"])
print("Title: " + emp["title"])

print("\nRunning command...\n")

cmd = "date"
sp.run(cmd)

print("")
cmd = "curl -V"
op = sp.run(cmd, stdout=sp.PIPE)
op = str(op)
print("res: " + op)

print("")
for o in op.split(","):
   if ( o.startswith(" stdout") ):
      o = o.replace("\\r\\n", "\n")
      print("res(fixed): " + o[10:-2])

print("\nTesting functions...\n")

def printMsg():
   if ( args.message ): print(args.message)
   else: print("This is a test")

def calcSum(a, b):
   s = a + b
   return s

print("Calling printMsg()...\nmessage: ", end='')
printMsg()
print("")

print("Calling calcSum() with 7 and 5...")
s = calcSum(7,5)
print("sum: " + str(s))

print("")
