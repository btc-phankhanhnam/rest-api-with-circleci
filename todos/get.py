import binascii
import random
import time
from datetime import datetime, timedelta, timezone


JST = timezone(timedelta(hours=+9))

class DateFormat:
  TIMEZONE = '%Y-%m-%dT%H:%M:%S.%fZ'
  YYYYMMDD = '%Y%m%d'
  YYYYMM = '%Y%m'
  YYYY_MM_DD = '%Y.%m.%d'
  YYYYMMDDHHMMSS = '%Y%m%d%H%M%S'

def timestampToDatetime(datetime_str):
  return datetime.strptime(datetime_str, DateFormat.TIMEZONE)

def correctTimezoneFormat(s):
  return s[:-4] + 'Z' if s else ''

def utcformat(dt, timespec='milliseconds'):
  iso_str = dt.astimezone(timezone.utc).isoformat('T', timespec)
  return iso_str.replace('+00:00', 'Z')

def timestamp():
  now = datetime.now(tz=timezone.utc)
  return utcformat(now)

def get_time_stamp(timestamp):
  publishedAtTime = timestampToDatetime(timestamp) + timedelta(milliseconds=1)
  publishedAt = correctTimezoneFormat(publishedAtTime.strftime(DateFormat.TIMEZONE))
  return get_time_stamp(publishedAt)

timex = timestamp()
for i in range(10):
  print(get_time_stamp(timex))
