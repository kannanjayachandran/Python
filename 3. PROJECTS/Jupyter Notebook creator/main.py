import os
from datetime import datetime


# checking current directory and creating a folder
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'Jupyter Notebooks')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)

today = datetime.today().strftime("%b-%d-%Y")

# Creating Jupyter file with current day as name
filepath = os.path.join(
    current_directory, final_directory, '%s.ipynb' % today)
if not os.path.exists(final_directory):
    os.makedirs(final_directory, today)
f = open(filepath, "a")
