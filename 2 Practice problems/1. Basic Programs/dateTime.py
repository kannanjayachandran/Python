#  Write a Python program to display the current date and time.

import datetime

now = datetime.datetime.now()
print("Current date and time is : ")
print(now.strftime("%d-%m-20%y %H:%M:%S"))
