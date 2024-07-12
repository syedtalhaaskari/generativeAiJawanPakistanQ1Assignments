# Write a program that takes a datetime object (naive) and a timezone name as input, and returns a localized datetime object in the specified timezone.

from datetime import datetime
import pytz

def localize_timezone(datetime_obj, tz):
    timezone = pytz.timezone(tz)
    return timezone.localize(datetime_obj)

timezones = [
    'Asia/Karachi',
    'America/New_York',
    'GMT+0',
    'Australia/Sydney'
]

datetime_obj = datetime.now()

for tz in timezones:
    localized_tz = localize_timezone(datetime_obj, tz)
    print(f"Initial date and time: {datetime_obj}")
    print(f"Localised date and time in {tz}: {localized_tz}\n")