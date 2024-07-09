# Write a program that calculates and displays the number of days between two given dates.

from datetime import date

def calculate_days(date1, date2):
    
    date1 = date.fromisoformat(date1)
    date2 = date.fromisoformat(date2)
    return (date1 - date2 if date1 > date2 else date2 - date1).days

dates = [
    {  
        'date1': "2015-01-16",
        'date2': "2015-01-16",
    },
    {  
        'date1': "2016-01-16",
        'date2': "2015-01-16",
    },
    {  
        'date1': "2016-01-16",
        'date2': "2017-01-16",
    },
]

for date_set in dates:
    date1, date2 = date_set.values()
    diff = calculate_days(date1, date2)
    print("Date 1: %s\nDate 2: %s" % (date1, date2))
    print("Days Difference: %s\n" % diff)