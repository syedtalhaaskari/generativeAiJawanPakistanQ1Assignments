# create a datetime object from the string "08-26-2023 08:10:00 PM"
# hint: https://strftime.org/

from datetime import datetime

def format_datetime(datetime_str):
    
    format = "%d-%m-%Y %I:%M:%S %p"
    
    return datetime.strptime(datetime_str, format)

datetime_str = '26-08-2023 08:10:00 PM'

formatted_datetime = format_datetime(datetime_str)

print(f"Date Time: {datetime_str}")
print(f"Formatted Date: {formatted_datetime}")