from datetime import date, datetime
import time
import random

date1 = input("Enter the first date: ")
date2 = input("Enter the second date: ")

date1 = date1.split("-")
date2 = date2.split("-")

try:
    d1 = date(int(date1[0]), int(date1[1]), int(date1[2]))
except:
    print("Wrong dates")
    exit()
print(d1)
try:
    d2 = date(int(date2[0]), int(date2[1]), int(date2[2]))
except:
    print("Wrong dates")
    exit()
print(d2)

try:
    d3 = random.randrange(time.mktime(d1.timetuple()) ,time.mktime(d2.timetuple()))
except:
    print("Wrong dates")
    exit()

current_time = time.localtime(d3)
final_time = time.strftime("%Y-%m-%d", current_time)
print("The random date:", final_time)
if current_time.tm_wday == 0: # Monday in Python is represented by the number 0
    print("I have no vinaigrette\n")
