# Write a program that calculates the time difference between two given datetime objects and displays it in hours, minutes, and seconds.

from datetime import datetime, timedelta

def calc_datetime_difference(datetime1, datetime2):
    datetime_obj_1 = datetime.fromisoformat(datetime1)
    datetime_obj_2 = datetime.fromisoformat(datetime2)
    difference = datetime_obj_1 - datetime_obj_2

    hours, remainder = divmod(difference.total_seconds(), 3600)
    minutes, remainder = divmod(remainder, 60)
    seconds = remainder
    
    return (abs(int(hours)), abs(int(minutes)), abs(int(seconds)))

datetime1 = '2001-12-30 12:30:17'
datetime2 = '2003-01-15 10:45:01'

difference = calc_datetime_difference(datetime1, datetime2)

print(f"Date Time 1: {datetime1}")
print(f"Date Time 2: {datetime2}")
print(f"Difference => Hours: {difference[0]}; Minutes: {difference[1]}; Seconds: {difference[2]}")