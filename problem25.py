# Create a function that takes a timezone name and a number of hours as input, and prints the current time plus the specified hours in that timezone

from datetime import datetime, timedelta
import pytz

def convert_timezone(tz, hours_to_add):
    current_datetime = datetime.now()

    timezone = pytz.timezone(tz)

    modified_datetime = current_datetime + timedelta(hours=hours_to_add)

    modified_datetime = modified_datetime.astimezone(timezone)

    print(f"Current DateTime: {current_datetime}")
    print(f"DateTime in {tz}: {modified_datetime}\n")

timezones = [
    'Asia/Karachi',
    'America/New_York',
    'GMT+0',
    'Australia/Sydney'
]

hours_to_add = 5

for tz in timezones:
    converted_tz = convert_timezone(tz, hours_to_add)