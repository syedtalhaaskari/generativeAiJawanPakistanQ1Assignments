# create a datetime object from the string "26-08-2023 15:18:33.983780-07:00" 
# hint: https://strftime.org/

from datetime import datetime

def format_datetime(datetime_str):
    
    format = "%d-%m-%Y %H:%M:%S.%f%z"
    
    return datetime.strptime(datetime_str, format)

datetime_str = '26-08-2023 15:18:33.983780-07:00'

formatted_datetime = format_datetime(datetime_str)

print(f"Date Time: {datetime_str}")
print(f"Formatted Date: {formatted_datetime}")