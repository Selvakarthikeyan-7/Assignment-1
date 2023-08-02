#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install requests


# In[ ]:


import requests

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = '3ae725b91c26108b346e35cd4a9eaa6d'
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast'
LOCATION = 'London,uk'

def get_weather_data(date):
    url = f"{BASE_URL}?q={LOCATION}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    for item in data['list']:
        dt_txt = item['dt_txt'].split()[0]
        if dt_txt == date:
            return item['main']['temp']
    return None

def get_wind_speed_data(date):
    url = f"{BASE_URL}?q={LOCATION}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    for item in data['list']:
        dt_txt = item['dt_txt'].split()[0]
        if dt_txt == date:
            return item['wind']['speed']
    return None

def get_pressure_data(date):
    url = f"{BASE_URL}?q={LOCATION}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    for item in data['list']:
        dt_txt = item['dt_txt'].split()[0]
        if dt_txt == date:
            return item['main']['pressure']
    return None

def main():
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = int(input("Enter your choice: "))

        if option == 0:
            print("Exiting the program.")
            break
        elif option == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            temp = get_weather_data(date)
            if temp is not None:
                print(f"The temperature on {date} is {temp:.2f} °C")
            else:
                print("Data not available for the given date.")
        elif option == 2:
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_data(date)
            if wind_speed is not None:
                print(f"The wind speed on {date} is {wind_speed} m/s")
            else:
                print("Data not available for the given date.")
        elif option == 3:
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_data(date)
            if pressure is not None:
                print(f"The pressure on {date} is {pressure} hPa")
            else:
                print("Data not available for the given date.")
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

