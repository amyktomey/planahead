import json
import requests
from datetime import datetime

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

#get today's date
now = datetime.now()

# convert date/time to string
daytime = now.strftime("%X %A %m/%d/%Y")
day = now.strftime("%A %m/%d/%Y")
day_name = now.strftime("%A")
time = now.strftime("%H:%M")

zip_code = (mydictionary[day_name]["zip"])

#use today's location for weather info
if  ("none") in mydictionary[day_name]["stop"]:
    print("The food truck is closed on the weekends.")

else:
    print(f"Good morning, {name}! Today is {day}, it's {time}. The food truck will be at: {mydictionary[day_name]['stop']}.")


# #weather forecast
if ("none") in mydictionary[day_name]["zip"]:
    print("No forecast today.")
else:
    api_key = "de1b3ad582a8ed4c1efb1e487c14480c"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    #use zip code from dictionary for weather information
    zip_code = (mydictionary[day_name]['zip'])

    final_url = base_url + "appid=" + api_key + "&zip=" + zip_code

    weather_data = requests.get(final_url)

    forecast = weather_data.json()

    kelvin = forecast["main"]["temp"]

    description = forecast["weather"][0]["description"]

    #convert Kelvin to Farenheight
    farenheight = ((kelvin * (9/5)) - 459.67)
    temp_is = str(round(farenheight,))

    print("\nTpday's temperature :", temp_is,chr(176)),
    print("\nForecast: ", description)