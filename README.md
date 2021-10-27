This app gives food :fork_and_knife: truck info and weather at scheduled locations.  :tada: :sparkles: :fireworks:

Dear user, if you haven't already...  please *'pip install requests'*. 

I stored location data in a **_json_** file.  This made updating easier, should the locations change or a special stop be made on the weekend.

Run truck_info.py
*(The file weather.py was used for testing purposes, only.)*

**Json** and **requests** install first.

Your name is requested. The program pauses, waiting for input.

A fucntion converts json files to dictionary files.

Today's date is captured using *datetime* and compared to the keys in the dictionary, giving the location based on the day of the week.

The weather API grabs the ***zip*** from the dictionary. Temperature is converted from Kelvin to Farenheight. 

Whew! Now, here are your results...

*(actual display)*

What is your name? Amy
Good morning, Amy! Today is Wednesday 10/27/2021, it's 10:28. The food truck will be at: TPUSA.

Temperature :  45.95

Forecast:  clear sky

:triumph: :tada: :sparkles: :fireworks: :sunglasses:

![Your Repository's Stats](https://github-readme-stats.vercel.app/api?username=amyktomey&show_icons=true)