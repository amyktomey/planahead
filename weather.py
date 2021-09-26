import requests
 
API_key = "de1b3ad582a8ed4c1efb1e487c14480c"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
zip_code = input("Enter a Zip code and country code : ")
Final_url = base_url + "appid=" + API_key + "&zip=" + zip_code
 
weather_data = requests.get(Final_url).json()

temp = weather_data['main']['temp']

description = weather_data['weather'][0]['description']

print('\nTemperature : ',temp)
print('\nDescription : ',description)