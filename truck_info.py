import json
import requests

#request input from user
name = input("What is your name? ")

#import locations from json/ set up dictionary
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

#get today's date
from datetime import datetime
now = datetime.now()

# convert date/time to string
daytime = now.strftime("%X %A %m/%d/%Y")
day = now.strftime("%A %m/%d/%Y")
day_name = now.strftime("%A")
time = now.strftime("%H:%M")
#print("Today is ", day)
#print("The time is ", time)

zip_code = (mydictionary[day_name]['zip'])
#print(mydictionary[day_name]['zip'])

#use today's location for weather info
if  ('none') in mydictionary[day_name]['stop']:
    print('The food truck is closed on the weekends.')

else:
    print(f"Good morning, {name}! Today is {day}, it's {time}. The food truck will be at: {mydictionary[day_name]['stop']}.")

# #weather forecast

if ('none') in mydictionary[day_name]['zip']:
    print('No forecast today.')
else:
    API_key = "de1b3ad582a8ed4c1efb1e487c14480c"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    #use zip code from dictionary for weather information
    zip_code = (mydictionary[day_name]['zip'])

    Final_url = base_url + "appid=" + API_key + "&zip=" + zip_code

    weather_data = requests.get(Final_url)
    #print(weather_data)

    forecast = weather_data.json()
    #print(forecast)

    temperature = forecast["main"]["temp"]

    description = forecast['weather'][0]['description']

    #convert Kelvin to Farenheight
    kel2far = ((temperature * (9/5)) - 459.67)
    tempis = str(round(kel2far, 2))

    print('\nTemperature : ', tempis),
    print('\nForecast: ', description)
  
#print menu items for the day