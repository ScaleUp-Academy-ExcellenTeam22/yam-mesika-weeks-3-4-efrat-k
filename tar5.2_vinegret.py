from datetime import date, datetime
import time
import random

"""
    @:param Date in Y-M-D format
    @:return Date in D-M-Y format
"""
def return_in_format(date1_from_user):
    try:
        datee = date1_from_user.split("-")
        date_in_format = date(int(datee[0]), int(datee[1]), int(datee[2]))
    except:
        print("Wrong dates")
        exit()
    return date_in_format


"""
    @:param Two dates
    @:return A  random date between these two dates
"""

def random_and_print(date1,date2):
    try:
        date3_in_format_between = random.randrange(time.mktime(date1.timetuple()) ,time.mktime(date2.timetuple()))
    except:
        print("Wrong dates")
        exit()
    current_time = time.localtime(date3_in_format_between)
    final_time = time.strftime("%Y-%m-%d", current_time)
    print("The random date:",final_time)
    return current_time

if __name__ =="__main__":
    date1_from_user = input("Enter the first date: ")
    date2_from_user  = input("Enter the second date: ")

    date1_in_format= return_in_format(date1_from_user)
    date2_in_format= return_in_format(date2_from_user)
    current_time=random_and_print(date1_in_format,date2_in_format)
    if current_time.tm_wday == 0:  # Monday in Python is represented by the number 0
        print("I have no vinaigrette")