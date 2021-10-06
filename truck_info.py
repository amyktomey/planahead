import json
import requests
#import weather

def convert_json_to_dict(myfilepathname):
    """get truck locations"""  
    try:
        with open(myfilepathname, "r") as read_file:
            my_new_dict =  dict(json.load(read_file))
            
    except:
        my_new_dict = {}
    
    return my_new_dict


#get today's date...
from datetime import datetime

# current date
now = datetime.now()

# convert to string
day = now.strftime("%A %m-%d-%Y")
day_name = now.strftime("%A")

print("Today is ", day)

#import truck location from json
mydictionary = convert_json_to_dict("locations.json")

print(mydictionary)

print(f"Today is {day_name}.  The food truck will be at, {mydictionary[day_name]['stop']}")
# if data requested on Saturday and Sunday
#f day_name
 #   else:
  #      print('The food truck is closed on the weekends.')

#weather forecast
#print('\nTemperature : ', tempis)

#print('\nDescription : ',description)
##print menu items for the day