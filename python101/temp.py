#
#
# Taking CSV in S3, counting the number of rows
#
# Authors: Michal Mendygral
#
#
from datetime import date, datetime, timedelta
import datetime
import bz2
from itertools import (takewhile, repeat)



x = "somevalue"

def func_A ():
   global x
   x = "siema"
   return x

def func_B():
   x = func_A()
   # Do things
   return x

print(x)

func_A()
func_B()

S3 ="/data/2020/2020-06/2020-06-19/extract-2020-06-19.csv.bz2"
filename  = "~/Downloads/extract-2020-06-19.csv.bz2"
def func_temp():
    return 12, (S3.split("/")[12]).split("-")[0]

print(func_temp()[1])

TODAY = str(date.today() + timedelta(days=-3))
print(TODAY)

dagrun_timeout = timedelta(minutes=60)

print (dagrun_timeout)


def rawincount(filepath):
   """
   Count the number of lines in a text file.
   Inspired from https://stackoverflow.com/a/27518377/798053
   """
   bufgen = None
   with bz2.open(filepath, 'rb') as f:
      bufgen = takewhile(lambda x: x, (f.read(1024 * 1024) for _ in repeat(None)))
      print(bufgen)
      print(sum(buf.count(b'\n') for buf in bufgen))
      return sum(buf.count(b'\n') for buf in bufgen)


rawincount(filename)

