# Create a function that takes a timezone name as input and prints the current date time object in that timezone.

from datetime import datetime
import pytz

def print_current_datetime_in_timezone(timezone_name):
    timezone = pytz.timezone(timezone_name)
    current_datetime = datetime.now(timezone)
    print(f"Current date and time in {timezone_name}: {current_datetime}\n")

timezones = [
    'Asia/Karachi',
    'America/New_York',
    'GMT+0',
    'Australia/Sydney'
]

for tz in timezones:
    print_current_datetime_in_timezone(tz)