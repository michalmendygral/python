#
#
# Taking CSV in S3, counting the number of rows, send the corresponding KPI onto ES
#
# Authors: Michal Mendygral, Denis Arnaud
#
#
from datetime import date, datetime, timedelta
import datetime
import bz2
from itertools import (takewhile, repeat)

#TODAY = str(datetime.today())
#TODAY_MONTH = str(datetime.today())[:-3]
#TODAY_YEAR = str(datetime.today()).split("-")[0]

# Exchange S3 bucket
#S3_URL_ROOT = "https://console.aws.amazon.com/s3/buckets/analytics-pr-s3-exchange/lake/ocean/volumes/aor"
#S3_URL_SUFFIX = "?region=eu-central-1&tab=overview#"
#S3_URL= S3_URL_ROOT + "/" + TODAY_YEAR + "/" + TODAY_MONTH + "/" + TODAY + "/" + S3_URL_SUFFIX
#S3_DIR = "/data/exchange/ocean/volumes/aor/" + TODAY_YEAR + "/" + TODAY_MONTH + "/" + TODAY + "/"
#S3_FILE = S3_DIR+"aor_volume_extract-"+TODAY+".csv.bz2"

#print(S3_FILE)
#content =""
#with bz2.open("/Users/michalmendygral/Downloads/aor_volume_extract-2020-06-15.csv.bz2", "rb") as f:
#    content = len(f.readlines())
#    print(content)

#with open("/Users/michalmendygral/Downloads/aor_volume_extract-2020-06-15.csv", "rb") as f:
#    content = len(f.readlines())
#    print(content)

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

S3 ="/data/bdp-all-shared/data/analytics/lake/ocean/volumes/aor/2020/2020-06/2020-06-19/aor_shpm_extract-2020-06-19.csv.bz2"
filename  = "/Users/michalmendygral/Downloads/aor_volume_extract-2020-06-19.csv.bz2"
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

