import requests, json, time



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

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    output =  current_time + ": It is " + str(round(current_temp, 0)) + " degrees fahrenheit in Tuscaloosa, AL with " + weather_desc
    return output 

