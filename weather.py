import requests
import json


API_key = "de1b3ad582a8ed4c1efb1e487c14480c"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

zip_code = input('Enter a zip Code:')

Final_url = base_url + "appid=" + API_key + "&zip=" + zip_code

weather_data = requests.get(Final_url)
#print(weather_data)

forecast = weather_data.json()
print(forecast)

kelvin = forecast["main"]["temp"]

description = forecast['weather'][0]['description']

#convert Kelvin to Farenheight
farenheight = ((kelvin * (9/5)) - 459.67)
temp_is = str(round(farenheight,))

print('\nTemperature : ', temp_is,chr(176)),
print('\nDescription : ', description)