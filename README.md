This app gives food :fork_and_knife: truck info and weather at scheduled locations.  :tada: :sparkles: :fireworks:

Dear user, if you haven't already...  please *'pip install requests'*. 

I stored location data in a **_json_** file.  This made updating easier, should the locations change or a special stop be made on the weekend.

Run truck_info.py
*(The file weather.py was used for testing purposes, only.)*

**Json** and **requests** install first.

Your name is requested. The program pauses, waiting for input.

A fucntion converts json files to dictionary files.

Today's date is captured using *datetime* and compared to the keys in the dictionary, giving the location based on the by day of the week.

The weather API grabs the ***zip*** from the dictionary. Temperature is converted from Kelvin to Farenheight. 

Whew! Now, here are your results...

*(actual display)*

What is your name? Amy
Good morning, Amy! Today is Tuesday.  The food truck will be at: GE.

Temperature :  69.26

Forecast:  scattered clouds

:triumph: :tada: :sparkles: :fireworks: :sunglasses:

![Your Repository's Stats](https://github-readme-stats.vercel.app/api?username=amyktomey&show_icons=true)