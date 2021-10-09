import json

#weather API function


#import truck location from json
def convert_json_to_dict(myfilepathname):
    """get truck locations"""  
    try:
        with open(myfilepathname, "r") as read_file:
            my_new_dict =  dict(json.load(read_file))            
    except:
        my_new_dict = {}    
    return my_new_dict

mydictionary = convert_json_to_dict("locations.json")
#print(mydictionary)

#get today's date...
from datetime import datetime
now = datetime.now()

# convert to string
day = now.strftime("%A %m-%d-%Y")
day_name = now.strftime("%A")

zip_code = (mydictionary[day_name]['zip'])
#print("Today is ", day)
#print(mydictionary[day_name]['zip'])
#today's location
if  ('none') in mydictionary[day_name]['stop']:
    print('The food truck is closed on the weekends.')
else:
    print(f"Today is {day_name}.  The food truck will be at: {mydictionary[day_name]['stop']}")

#weather forecast
from weather import get_weather 

zip_code = (mydictionary[day_name]['zip'])
#print (zip_code)

if zip_code == (""): #(mydictionary[day_name]['zip']):
    print('No forecast today.')
else:
    zip_code == (mydictionary[day_name]['zip'])
    get_weather()

    
#print menu items for the day