#food truck locations, Monday through Friday
location = {'Monday':'U of L',
            'Tuedsay':'GE',
            'Wednesday':'TPUSA',
            'Thursday': 'Jefferson Mall',
            'Friday':'Big 4 Bridge'}
location_zip = {40292, 40228, 40223, 40219, 40245}
#get today's date...
from datetime import datetime

# current date
now = datetime.now()

# convert to string
today = now.strftime("%A-%m-%d-%Y")
day_name = now.strftime("%A")
print('Today is ', today)
if day_name == ('Saturday' or 'Sunday'):
    print("I'm sorry, the food truck is closed on the weekend.")
else:
    day_name != ('Saturday' or 'Sunday')
    
    print("The food truck is at ", location.item, today)


#food truck is closed on Saturday and Sunday
#error if data requested on Saturday and Sunday


#weather forecast for any calendar day by zipcode

#Menu pre order here (inventory assist) while loop