class WeatherDataFetcher:
    def __init__(self):
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }

    def fetch_weather_data(self, city):
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, {})


class DataParser:
    def parse_weather_data(self, data):
        if not data:
            return "Weather data not available"
        city = data.get("city", "Unknown")
        temperature = data.get("temperature", "N/A")
        condition = data.get("condition", "N/A")
        humidity = data.get("humidity", "N/A")
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"


class UserInterface:
    def __init__(self):
        self.fetcher = WeatherDataFetcher()
        self.parser = DataParser()
        self.start() 

    def get_detailed_forecast(self, city):
        data = self.fetcher.fetch_weather_data(city)
        return self.parser.parse_weather_data(data)

    def display_weather(self, city):
        data = self.fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            print(self.parser.parse_weather_data(data))

    def start(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                print(self.get_detailed_forecast(city))
            else:
                self.display_weather(city)


UserInterface()
