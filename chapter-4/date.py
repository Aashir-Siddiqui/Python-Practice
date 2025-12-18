from datetime import date, time, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

x = datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

y = datetime(2020, 9, 18)
print(y)

today = date.today()
print("Today's date:", today)
print(today.year)
print(today.month)
print(today.day)

t = time(14, 30, 45)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

today = datetime.now()
future = today + timedelta(days=7)
past = today - timedelta(days=30)

print(future)
print(past)


utc_now = datetime.now(timezone.utc)
print("UTC time:", utc_now)

pak_time = utc_now.astimezone(ZoneInfo("Asia/Karachi"))
print("Pak time:", pak_time)

dob = datetime(2000, 1, 1)
today = datetime.now()

now = datetime.now()
timestamp = now.timestamp()
print(timestamp)

age = today.year - dob.year
print(age)



# Directive	 |   Description	  |    Example
# %a	 |   Weekday, short version	  |    Wed	
# %A	 |   Weekday, full version	  |    Wednesday	
# %w	 |   Weekday as a number 0-6, 0 is Sunday	  |    3	
# %d	 |   Day of month 01-31	  |    31	
# %b	 |   Month name, short version	  |    Dec	
# %B	 |   Month name, full version	  |    December	
# %m	 |   Month as a number 01-12	12	
# %y	 |   Year, short version, without century	  |    18	
# %Y	 |   Year, full version	  |    2018	
# %H	 |   Hour 00-23	  |    17	
# %I	 |   Hour 00-12	  |    05	
# %p	 |   AM/PM	  |    PM	
# %M	 |   Minute 00-59	  |    41	
# %S	 |   Second 00-59	  |    08	
# %f	 |   Microsecond 000000-999999	  |    548513	
# %z	 |   UTC offset	  |    +0100	
# %Z	 |   Timezone	  |    CST	
# %j	 |   Day number of year 001-366	  |    365	
# %U	 |   Week number of year, Sunday as the first day of week, 00-53	  |    52	
# %W	 |   Week number of year, Monday as the first day of week, 00-53	  |    52	
# %c	 |   Local version of date and time	Mon Dec 31 17:41:00   |    2018	
# %C	 |   Century	  |    20	
# %x	 |   Local version of date	  |    12/31/18	
# %X	 |   Local version of time	  |    17:41:00	
# %%	 |   A % character	  |    %	
# %G	 |   ISO 8601 year	  |    2018	
# %u	 |   ISO 8601 weekday (1-7)	  |    1	
# %V	 |   ISO 8601 weeknumber (01-53)	  |    01
