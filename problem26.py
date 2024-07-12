# Write a program that calculates the date and time of the daylight saving start in the year 2022.
# take timezone "US/Pacific"
# take string date as "2022-01-01 00:00:00"
# hint: use
# bool(tz_aware_dt.dst()) == True # dst activated
# bool(tz_aware_dt.dst()) == False # dst not activated

string_date = "2022-01-01 00:00:00"

from datetime import datetime, timedelta
import pytz

def calculate_dst_start(timezone_name, date_str):
    tz = pytz.timezone(timezone_name)

    date_obj = datetime.fromisoformat(date_str)

    # convert to timezone aware datetime

    tz_aware_dt = tz.localize(date_obj)

    return 'not activated' if tz_aware_dt.dst() else 'activated'

tz = "US/Pacific"

date_str = "2023-01-01 00:00:00"

isActivated = calculate_dst_start(tz, date_str)

print(f"Day light saving in time zone {tz} on date {date_str} is {isActivated}")
