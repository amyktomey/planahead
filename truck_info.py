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
    print(f"Good morning, {day_name}!  The food truck will be at: {mydictionary[day_name]['stop']}.")

#weather forecast
#import weather #import get_weather 

#zip_code = (mydictionary[day_name]['zip'])
#print (zip_code)

if zip_code == (mydictionary[day_name]['zip']):
    import weather
    import requests
    API_key = "de1b3ad582a8ed4c1efb1e487c14480c"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    #get zip code from dictionary
    zip_code = (mydictionary[day_name]['zip'])

    Final_url = base_url + "appid=" + API_key + "&zip=" + zip_code

    weather_data = requests.get(Final_url)

    #print(weather_data)

    forecast = weather_data.json()
    #print(forecast)

    temp = forecast["main"]["temp"]

    description = forecast['weather'][0]['description']

    #convert Kelvin to Farenheight
    kel2far = ((temp * (9/5)) - 459.67)
    tempis = str(round(kel2far, 2))

    print('\nTemperature : ', tempis),
    print('\nDescription : ', description)
else:   
    print('No forecast today.')

    
   

    
#print menu items for the day