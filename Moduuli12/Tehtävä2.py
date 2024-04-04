import requests
from geopy.geocoders import Nominatim



def get_weather(city):
    geolocattor = Nominatim(user_agent="city")
    location = geolocattor.geocode(city)

    if location:
        lat = location.latitude
        long = location.longitude
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=b9f2025e123058031a656b93f56153ec")

        if response.status_code == 200:
            data = response.json()
            celsius = data["main"]["temp"] - 273.15
            current_weather = data["weather"][0]["description"]
            print(f"The current weather in {city} is:\n{current_weather.capitalize()}\nTemperature: {celsius:.2f} C")
        else:
            print("Säätilan hakeminen epäonnistui.")



city = input('anna kaupunki')
get_weather(city)