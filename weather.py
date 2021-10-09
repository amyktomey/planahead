import requests

def get_weather():
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