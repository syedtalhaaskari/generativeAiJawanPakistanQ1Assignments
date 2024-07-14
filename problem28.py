# Design a program that helps schedule a meeting across different timezones. The program should take the meeting time in one timezone and display the corresponding times in other timezones.
# consider three countries: UK, US, Saudi Arab and Pakistan
# consider the meeting time is: 30 August 2023 at 2 PM Pakistan time

from datetime import datetime, timedelta
import pytz

def calc_meeting_datetime(meeting_datetime: str, tz):
    timezones = [
        "GMT0", # For UK
        "US/Central", # For US
        "Asia/Riyadh", # For Saudi Arab
        "Asia/Karachi", # For Pakistan
    ]
    format = '%d %B %Y at %I %p'
    c_tz = pytz.timezone(tz)
    meeting_datetime_obj = c_tz.localize(datetime.fromisoformat(meeting_datetime))
    for _tz in timezones:
        if _tz == tz:
            continue
        change_tz = pytz.timezone(_tz)
        meeting_datetime_obj = meeting_datetime_obj.astimezone(change_tz)
        f_meeting_datetime = datetime.strftime(meeting_datetime_obj, format)
        print(f"Meeting datetime: in {_tz}: {f_meeting_datetime}")
                        
meeting_datetime = "2023-08-30 14:00:00"
tz = "Asia/Karachi"

format = '%d %B %Y at %I %p'
meeting_datetime_obj = datetime.fromisoformat(meeting_datetime)
f_meeting_datetime = datetime.strftime(meeting_datetime_obj, format)

print(f"Current meeting datetime in {tz}: {f_meeting_datetime}")

calc_meeting_datetime(meeting_datetime, tz)