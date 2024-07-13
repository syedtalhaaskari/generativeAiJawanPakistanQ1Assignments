# dt_named_and_short_form_format = "8-August-23 08:10:00"
# hint: https://strftime.org/

from datetime import datetime

def format_datetime(datetime_str):
    
    format = "%d-%B-%y %H:%M:%S"
    
    return datetime.strptime(datetime_str, format)

datetime_str = '8-August-23 08:10:00'

dt_named_and_short_form_format = format_datetime(datetime_str)

print(f"Date Time: {datetime_str}")
print(f"Formatted Date: {dt_named_and_short_form_format}")