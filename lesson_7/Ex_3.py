import requests
from datetime import datetime

keys = open("keys.txt", "r")
API_KEY = keys.read()

city_name = input("Enter city name: ")
number_of_days = int(input("Enter number of days: "))

weather_data = requests.get(
    f"http://api.openweathermap.org/data/2.5/forecast/daily?q={city_name}&cnt={number_of_days}&appid={API_KEY}")

forecast = weather_data.json()

new_file = open("Odessa-5-days-weather-forecast.txt", "w")
new_file.write("|Date       |Temperature at day |Temperature at night |Feels like at day  |Feels like at night|")

for day in forecast["list"]:
    new_file.write("\n" + "|" + str(datetime.fromtimestamp(day["dt"]).strftime("%d-%m-%Y |")) +
                   str(round(day["temp"]["day"] - 273.15)) + "°C               |" +
                   str(round(day["temp"]["night"] - 273.15)) + "°C                 |" +
                   str(round(day["feels_like"]["day"] - 273.15)) + "°C               |" +
                   str(round(day["feels_like"]["night"] - 273.15)) + "°C               |")
