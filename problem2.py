# Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".

from datetime import datetime

def print_current_date(_date):
    format = "%m/%d/%Y"
    current_date = datetime.strptime(_date, format).date()
    print(current_date)

print_current_date('11/20/2015')