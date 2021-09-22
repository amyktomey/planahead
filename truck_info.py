#food truck locations, Monday through Friday, closed Saturday and Sunday in JSON

#get today's date...
from datetime import datetime

# current date
now = datetime.now()

# convert to string
today = now.strftime("%A %m-%d-%Y")
day_name = now.strftime("%A")

#error if data requested on Saturday and Sunday


print('Today is', today)

#weather forecast for today by zipcode

#Menu pre order here (inventory assist) while loop