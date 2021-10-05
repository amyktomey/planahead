import json
import requests

import weather

#get today's date...
from datetime import datetime

# current date
now = datetime.now()

# convert to string
day = now.strftime("%A %m-%d-%Y")
day_name = now.strftime("%A")

print("Today is ", day)

#import truck location from json

    print('Today is', day_name,'.  The food truck will be at', [stop])
#error if data requested on Saturday and Sunday
    else:

    print('The food truck is closed on the weekends.')

#weather forecast
#print('\nTemperature : ', tempis)

#print('\nDescription : ',description)
##print menu items for the day