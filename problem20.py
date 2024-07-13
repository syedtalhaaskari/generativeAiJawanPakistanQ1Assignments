# Write a program that takes a user-entered date in the format "MM/DD/YYYY" and prints it in the format "YYYY-MM-DD".

from datetime import datetime

def format_date(input_date):
    date_elems = input_date.split('/')
    date_obj = datetime(year=int(date_elems[2]), month=int(date_elems[0]), day=int(date_elems[1]))
    format = "%Y-%m-%d"
    
    formatted_date = datetime.strftime(date_obj, format)
    
    return formatted_date

input_date = input("Enter date (MM/DD/YYYY): ")

formatted_date = format_date(input_date)

print(f"Input Date: {input_date}")
print(f"Formatted Date: {formatted_date}")