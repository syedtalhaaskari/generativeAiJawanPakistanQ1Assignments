# Booking System
# Design a booking system where users specify a start datetime, end datetime, and timezone. Implement a function that checks whether a specified time slot is available.
# if timeslot is available then store the start_date and end_date in the list of objects i.e
"""
booking_storage = [
  {
    "start_date": "",
    "end_date": ""
  }
]
"""
# hint 1: store dates in booking_storage in UTC format i.e pytz.utc
# hint 2: use for loop, the loop should run 5 times. ask user input inside the loop

# instruction to test your program:
# first iteration of loop
# give input "2023-08-26 18:00:00" as start_date and "2023-08-26 19:00:00" as end_date and "Asia/Karachi" as timezone

# second iteration of loop
# give input "2023-08-26 16:00:00" as start_date and "2023-08-26 17:00:00" as end_date and "Asia/Riyadh" as timezone
# above program should not accept this booking as the slot is already booked by the first iteration

from datetime import datetime
import pytz

main_tz = "Asia/Karachi"
main_tz_obj = pytz.timezone(main_tz)
us_p_tz = pytz.timezone("US/Pacific")
us_c_tz = pytz.timezone("US/Central")


booking_storage = [
    # {
    #     'start_date': main_tz_obj.localize(datetime(2023, 8, 26, 18, 0)), 
    #     'end_date': main_tz_obj.localize(datetime(2023, 8, 26, 19, 0))
    # }, 
    # {
    #     'start_date': us_p_tz.localize(datetime(2023, 8, 26, 18, 0)), 
    #     'end_date': us_p_tz.localize(datetime(2023, 8, 26, 19, 0))
    # }, 
    # {
    #     'start_date': us_c_tz.localize(datetime(2023, 8, 26, 10, 0)), 
    #     'end_date': us_c_tz.localize(datetime(2023, 8, 26, 11, 0))
    # }
]

def calc_slot_availability(start_date_obj: datetime, end_date_obj: datetime):
    for item in booking_storage:
        if (start_date_obj >= item['start_date'] and start_date_obj <= item['end_date']) or (end_date_obj >= item['start_date'] and end_date_obj <= item['end_date']):
            print("The specified time slot is already booked.")
            return
    booking_storage.append({
        "start_date": start_date_obj,
        "end_date": end_date_obj
    })
    print("Booking Confirmed")

def get_input():
    start_date = input("\nEnter start date and time in (YYYY-MM-DD HH:MM:SS) format: ")
    end_date = input("Enter end date and time in (YYYY-MM-DD HH:MM:SS) format: ")
    timezone_input = input("Enter timezone (e.g., Asia/Karachi): ")
    timezone = pytz.timezone(timezone_input)
    start_date_obj = datetime.fromisoformat(start_date)
    start_date_obj = timezone.localize(start_date_obj)
    end_date_obj = datetime.fromisoformat(end_date)
    end_date_obj = timezone.localize(end_date_obj)
    return start_date_obj, end_date_obj
    
for i in range(5):
    start_date_obj, end_date_obj = get_input()
    
    calc_slot_availability(start_date_obj, end_date_obj)
    
for item in booking_storage:
    format = "%d %B %Y %I:%M:%S %p %Z"
    start_date_str = datetime.strftime(item['start_date'], format)
    end_date_str = datetime.strftime(item['end_date'], format)
    print(f"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(f"Start Date: {start_date_str} End Date: {end_date_str}")