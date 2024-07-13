# Write a program that converts a given date time (tz aware) string from one timezone to another.

from datetime import datetime
import pytz

def convert_timezone(date_obj, tz):
    timezone = pytz.timezone(tz)
    return date_obj.astimezone(timezone)

timezones = [
    'Asia/Karachi',
    'America/New_York',
    'GMT+0',
    'Australia/Sydney'
]

date_obj = datetime.now()

for tz in timezones:
    converted_tz = convert_timezone(date_obj, tz)
    print(f"Initial date and time: {date_obj}")
    print(f"Converted date and time in {tz}: {converted_tz}\n")