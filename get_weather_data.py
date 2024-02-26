import requests

def get_weather_data(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def main():
    # API key for OpenWeatherMap
    api_key = "YOUR_API_KEY_HERE"
    city = "New York"  # Example city
    
    # Call the function to get weather data
    weather_data = get_weather_data(api_key, city)
    
    # Print the weather data
    if weather_data:
        print("Weather Data:")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather: {weather_data['weather'][0]['description']}")

if __name__ == "__main__":
    main()
