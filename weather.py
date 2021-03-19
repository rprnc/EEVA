# Uses OpenWeatherMap API to get current weather conditions for any city
# Goofy way of reporting it and would be nice to have more detail
# Also this is fugly code, clean this up
# Add surf reports in to cities that have surf nearby


import requests


def weather_report(city_name):

    api_key = "#insert openweather api key here"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_temperature = round(current_temperature - 273, 1)
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]

        report = ('The weather in ' + city_name + ' is ok, the temperature in celsius is ' +
                  str(current_temperature) +
                  "\n humidity is " +
                  str(current_humidity) + 'percent'
                  "\n General description is " +
                  str(weather_description))

        return report
