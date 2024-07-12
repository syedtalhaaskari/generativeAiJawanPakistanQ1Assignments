# Create a function that takes a datetime object as input and displays the day of the week (e.g., "Monday") using strftime().
# hint: https://strftime.org/

from datetime import datetime

def return_day_name(datetime_obj):
    format = "%A"
    
    formatted_date = datetime.strftime(datetime_obj, format)
    
    return formatted_date

datetime_obj = datetime.now()

day_name = return_day_name(datetime_obj)

print(f"Date Time: {datetime_obj}")
print(f"Day Name: {day_name}")