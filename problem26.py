# Write a program that calculates the date and time of the daylight saving start in the year 2022.
# take timezone "US/Pacific"
# take string date as "2022-01-01 00:00:00"
# hint: use
# bool(tz_aware_dt.dst()) == True # dst activated
# bool(tz_aware_dt.dst()) == False # dst not activated

from datetime import datetime, timedelta
import pytz

def calc_dst_start(year: datetime, tz):
    tz = pytz.timezone(tz)
    for i in range(1,13):
        us_time = datetime(year=year, month=i, day=1)
        us_time = tz.localize(us_time)
        if us_time.dst().total_seconds() > 0:
            while True:
                us_time = us_time - timedelta(days=1)
                us_time = datetime(year=year, month=us_time.month, day=us_time.day)
                us_time = tz.localize(us_time)

                if us_time.dst().total_seconds() == 0:
                    while True:
                        us_time = us_time + timedelta(hours=1)
                        us_time = datetime(year=year, month=us_time.month, day=us_time.day, hour=us_time.hour)
                        us_time = tz.localize(us_time)
                        if us_time.dst().total_seconds() > 0:
                            return us_time
                        
year = 2022
tz = "US/Pacific"
dst_start = calc_dst_start(year, tz)

print(f"Daylight Saving Time for {tz} for the year {year} will start at {dst_start}")