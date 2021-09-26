import weather
import json

#food truck locations
class loc_data:
    def __init__(today, stop, zip):
        def from_json(json_string):
            json_dict = json.loads(json_string)
            return loc_data(**json_dict)

#get today's date...
from datetime import datetime

# current date
now = datetime.now()

# convert to string
day = now.strftime("%A %m-%d-%Y")
day_name = now.strftime("%A")

#error if data requested on Saturday and Sunday


print('Today is', day)

#weather forecast for today by zipcode
#print("\nThe weather today at " + zip_code +":\n")

#Menu pre order here (inventory assist) while loop