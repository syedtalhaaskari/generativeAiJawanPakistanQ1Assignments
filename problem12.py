# Create a function that takes a datetime object and a number of hours as input, then returns a new datetime object with the added hours.

from datetime import datetime, timedelta

def add_hours_in_datetime(datetime_obj, hours_to_add):
    add_datetime_obj = datetime_obj + timedelta(hours=hours_to_add)
    
    return add_datetime_obj

datetime_obj = datetime.fromisoformat('2001-12-30 12:30:17')
hours_to_add = 6

modified_datetime = add_hours_in_datetime(datetime_obj, hours_to_add)

print(f"Date Time: {datetime_obj}")
print(f"Hours to Add: {hours_to_add}")
print(f"Modified Date: {modified_datetime}")