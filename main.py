"""
Python Script to request the API for wheather forecast based on
1.Zipcodes
2.City
3.Latitude and Longitude
"""


import requests
import config

# 1.API key which is used the grab the data get u r api key here = https://home.openweathermap.org/api_keys


class Wheather:
    def __init__(self):
        self.api_key = config.API_KEY
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def zipcodes(self):
        zipcode = input("Enter the zipcode=")
        countrycode = input("Enter the country code like India:in , USA:us=")

        url = self.base_url + 'zip=' + zipcode + ',' + countrycode + '&appid=' + self.api_key
        weather_data = requests.get(url).json()

        print("\nCurrent Weather Data of " + zipcode + ":\n")
        print(weather_data)

    def citynames(self):
        cityname = input("Enter the city name=")

        # statecode = input("Enter the state=")
        # countrycode = input("Enter the country code like India:in,USA:usa=")

        url = self.base_url + cityname + '&appid=' + self.api_key
        weather_data = requests.get(url).json()

        print("\nCurrent Weather Data of " + cityname + ":\n")
        print(weather_data)

    def latlong(self):
        lat = input("Enter latitude=")
        lon = input("Enter longitude=")
        url = self.base_url + 'lat=' + lat + '&lon=' + lon + '&appid=' + self.api_key
        weather_data = requests.get(url).json()

        print("\nWeather Data By Geograhic Coordinates of :", lat, lon)
        print(weather_data)


print("Choices:\n1.Zipcode\n2.CityName\n3.Latitude and Longitude\n")
choice = int(input("Enter your choice="))

# 2.Creating a forecast object of Wheather class
forecast = Wheather()

if choice == 1:
    forecast.zipcodes()

if choice == 2:
    forecast.citynames()

if choice == 3:
    forecast.latlong()