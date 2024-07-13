# Create a function that takes a datetime in the format "MM/DD/YYYY HH:MM:SS" as string  formats it as "YYYY-MM-DD HH:MM:SS".

from datetime import datetime

def calc_datetime(bef_datetime):
    format = "%m/%d/%Y %H:%M:%S"
    iso_datetime = datetime.strptime(bef_datetime, format)
    # formatted_datetime = iso_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return iso_datetime

bef_datetime = '12/30/2001 12:30:17'

iso_datetime = calc_datetime(bef_datetime)

print(f"Date Time: {bef_datetime}")
print(f"Formatted datetime: {iso_datetime}")