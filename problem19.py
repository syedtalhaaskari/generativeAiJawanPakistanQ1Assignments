# create a current datetime and then displays it in the format "HH:MM AM/PM"

from datetime import datetime

def format_current_time():
    current_date = datetime.now()
    format = "%I:%M %p"
    
    return datetime.strftime(current_date, format)

formatted_current_time = format_current_time()

print(f"Formatted Current Time: {formatted_current_time}")