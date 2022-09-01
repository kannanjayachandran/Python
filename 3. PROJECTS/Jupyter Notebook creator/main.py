import os
from datetime import datetime


today = datetime.today().strftime("%b-%d-%Y")

filepath = os.path.join(
    'C:/Users/kanna/Documents/25. Practice/FILESS', '%s.ipynb' % today)
if not os.path.exists('C:/Users/kanna/Documents/25. Practice/FILESS'):
    os.makedirs('C:/Users/kanna/Documents/25. Practice/FILESS')
f = open(filepath, "a")
