import datetime
import random
print("#1-------------")
date_now = datetime.date.today()
print(date_now)
print("#2-------------")
date_today = datetime.datetime.today()
future = datetime.timedelta(days=15)
print(date_today + future)
print('#3-------------')
bday = datetime.date(2022, 5, 9)
day_today = datetime.date.today()
print((bday - day_today).days, "days till birthday")
print('#4-------------')
d = datetime.date.today().strftime("%A")
print(d)
print('#5-------------')
times = datetime.datetime.now()
t = times.strftime("%I:%M:%S %p")
print(t)
print('#6-------------')
current = datetime.datetime.today()
past = datetime.timedelta(days=random.randrange(-15, -7))
passed = current + past
print(passed)
print('#7-------------')
get_time = datetime.datetime(2018, 6, 1)

print(get_time.strftime("%C"))




