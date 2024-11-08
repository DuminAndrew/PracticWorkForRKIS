import json
import requests
import sys
from datetime import datetime

class Weather:
    def __init__(self, city, temp, description):
        self.city = city
        self.temp = temp
        self.description = description
        self.date = datetime.now().strftime('%Y-%m-%d')

    def to_dict(self):
        return {
            'city': self.city,
            'temp': self.temp,
            'description': self.description,
            'date': self.date
        }

class WeatherManager:
    def __init__(self, filename='weather_history.json'):
        self.filename = filename
        self.history = self.load_history()

    def load_history(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_history(self):
        with open(self.filename, 'w') as file:
            json.dump(self.history, file)

    def add_weather(self, weather):
        self.history.append(weather.to_dict())
        self.save_history()

    def get_history(self):
        return self.history

class WeatherService:
    API_URL = "http://api.openweathermap.org/data/2.5/weather"
    API_KEY = "f21b32b88551e9568aeb4d413fc84232"

    @staticmethod
    def get_weather(city):
        params = {
            'q': city,
            'appid': WeatherService.API_KEY,
            'units': 'metric',
            'lang': 'ru'
        }
        response = requests.get(WeatherService.API_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            return Weather(city, temp, description)
        return None

def main():
    default_city = "Москва"
    city = sys.argv[1] if len(sys.argv) > 1 else default_city
    weather_service = WeatherService()
    weather_manager = WeatherManager()

    weather = weather_service.get_weather(city)
    if weather:
        print(f"Погода в {weather.city} на {weather.date}: {weather.temp}°C, {weather.description}")
        weather_manager.add_weather(weather)
    else:
        print("Не удалось получить данные о погоде.")

if __name__ == "__main__":
    main()
