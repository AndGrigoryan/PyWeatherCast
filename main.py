#!/usr/bin/env python3

from decouple import config
import argparse
import json
from urllib.request import urlopen
from math import ceil


def open_url(url):
    try:
        with urlopen(url) as response:
            return response.read()
    except Exception as error:
        print(error)
        exit()


def get_url(city_name, api_key):
    return f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"


def get_data(src):
    return json.loads(src)


def display_weather_info(data, params):
    md = {}
    
    md["name"] = data['name']
    md["weather"] = data['weather'][0]['description']
    md["temperature"] = str(ceil(data['main']['temp'])) + "°C"
    md["wind_speed"] = data['wind']['speed']
    md["humidity"] = data['main']['humidity']


    if params == None:
        print("Today the weather in %s is %s\nwith temp %s, Wind speed %s m/s and Humidity %s%%" %(md["name"], md["weather"], md["temperature"], md["wind_speed"], md["humidity"]))
    else:
        for k, v in md.items():
            if k == "name":
                print("Today the weather in %s" %md['name'])
            if k in params:
                print("%s: %s" %(" ".join(k.split("_")).capitalize(), v))


def main():
    api_key = config('API_KEY')

    parser = argparse.ArgumentParser(description="Get city name and other parameters.")
    parser.add_argument("city", type=str, help="City name for weather search")
    parser.add_argument("--parameters", nargs="+", type=str, help="Other parameters for weather(temperature, humidity, etc…)")

    args = parser.parse_args()

    city_name, params = "%20".join(args.city.split()), args.parameters
    
    
    url = get_url(city_name, api_key) 
    src = open_url(url)
    data = get_data(src)    

    display_weather_info(data, params)


if __name__ == "__main__":
    main()

