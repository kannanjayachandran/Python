#  Write a Python program to display the current date and time.

import datetime

now = datetime.datetime.now()
print("Current date and time is : ")
print(now.strftime("%y-%m-%d %H:%M:%S"))
