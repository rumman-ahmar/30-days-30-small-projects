# pip install streamlit requests

import requests
import streamlit as st

# your api key
API_KEY = "5a90783600944cb2b2e8f1bad635a9f8"

# set the title of the webpage
st.title("Weathery: A weather application")
# create an input box to get the city
city = st.text_input("City", placeholder="London", value="London")


url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
weather_data = requests.get(url)

# check the api status code
api_status_code = weather_data.status_code
print(f"API status code is {api_status_code}")

# if the status code is 200 OK, create UI widgets to show the weather information
if api_status_code == 200:
    # convert API response into json
    weather_data = weather_data.json()
    # make a variable to store temperature
    temperature = weather_data['main']['temp']
    # make a variable to store feels like temperature
    feels_like = weather_data['main']['feels_like']
    # make a variable to store minimum temperature
    temp_min = weather_data['main']['temp_min']
    # make a variable to store maximum temperature
    temp_max = weather_data['main']['temp_max']
    # make a variable to store pressure
    pressure = weather_data['main']['pressure']
    # make a variable to store humidity
    humidity = weather_data['main']['humidity']
    # make a variable to store wind speed
    wind_speed = weather_data['wind']['speed']

    # create bootstrap columns
    first_col, second_col = st.columns(2)
    # show temperature
    first_col.write(f'Current temperature is: {temperature}°C')
    # show feels like temperature
    second_col.write(f'Feels like: {feels_like}°C')

    # create bootstrap columns
    first_col, second_col = st.columns(2)
    # show wind speed
    first_col.write(f'Wind speed is: {wind_speed}km/h')
    # show pressure
    second_col.write(f'Pressure is: {pressure}Pascal')

    # create bootstrap columns
    first_col, second_col = st.columns(2)
    # show minimum temperature
    first_col.write(f'Minimum temperature is: {temp_min}°C')
    # show maximum temperature
    second_col.write(f'Maximum temperature is: {temp_max}°C')

    # create bootstrap columns
    first_col, second_col = st.columns(2)
    # show humidity
    first_col.write(f'Humidity: {humidity}g.kg-1')

# API is not working properly
else:
    st.write("Something went wrong. Please try again.")
