# Create a program that takes a date as string and returns the corresponding day of the week (e.g., Monday, Tuesday, etc.).

from datetime import date


def return_day_name(_date):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    date_obj = date.fromisoformat(_date)
    day_ind = date_obj.weekday()
    return days[day_ind]

dates = [
    "2015-01-01",
    "2015-01-02",
    "2015-01-03",
    "2015-01-04",
    "2015-01-05",
    "2015-01-06",
    "2015-01-07",
    "2015-01-08",
]

for _date in dates:
    print(f"Date: {_date}")
    print(f"Day: {return_day_name(_date)}\n")