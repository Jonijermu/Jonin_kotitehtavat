import requests

import requests

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?name={city}&appid=b9f2025e123058031a656b93f56153ec"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_description = data["weather"]['main']
        temperature_kelvin = data['main']['temp']
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)
        print(f"Sää paikkakunnalla {city}: {weather_description}")
        print(f"Lämpötila: {temperature_celsius:.2f} °C")
    else:
        print("Säätilan hakeminen epäonnistui.")

def main():
    city = input("Syötä paikkakunnan nimi: ")
    get_weather(city)

if __name__ == "__main__":
    main()