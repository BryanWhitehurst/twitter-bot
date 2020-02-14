import requests, json
from datetime import datetime
import pytz


def getMsg():
    api_key = "6d1bb05fca4a5354af4b04f27a3f0479"
    url = "http://api.openweathermap.org/data/2.5/weather?appid=6d1bb05fca4a5354af4b04f27a3f0479&q=Tuscaloosa"
    response = requests.get(url)

    x = response.json()

    y = x["main"]
    current_temp = y["temp"]
    current_temp = (current_temp - 273.15)*(9/5) + 32
    z = x["weather"]
    weather_desc = z[0]["description"]

    tz = pytz.timezone('America/Chicago')
    tz_Chicago = datetime.now(tz)
    time = tz_Chicago.strftime("%H:%M:%S")
    timeList = time.split(':')
    hour = int(timeList[0])
    mins = int(timeList[1])
    
    if hour > 12:
        hour = hour - 12
        time = str(hour) + ":" + str(mins) + " PM"
        if mins < 10:
            time = str(hour) + ":" + "0" + str(mins) + " PM"
    else:
        time = str(hour) + ":" + str(mins) + " AM"
        if mins < 10:
            time = str(hour) + ":" + "0" + str(mins) + " AM"

    output =  time + ": It is " + str(round(current_temp, 0)) + " degrees fahrenheit in Tuscaloosa, AL with " + weather_desc + "."
    return output 

