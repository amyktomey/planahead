This app will give food truck data; weather at scheduled locations. 

**The file weather.py was used for testing purposes.

Run truck_info.py. 
Json and requests are imported at the top of the file truck_info.py.

Location information is stored in locations.json, to make updating easier. Json data is used to make a dicionary.

Location data is called by day of the week.

The weather api takes the zip from the dictionary and gives a forecast.  Temperature is converted from Kelvin to Farenheight.