import sqlite3

def create_weather_table(conn):
    """Create a SQLite table to store weather data."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY,
            city TEXT,
            temperature REAL,
            humidity REAL,
            weather_description TEXT
        )
    ''')
    conn.commit()

def store_weather_data(conn, data):
    """Store weather data in the SQLite database."""
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather (city, temperature, humidity, weather_description)
        VALUES (?, ?, ?, ?)
    ''', (data['name'], data['main']['temp'], data['main']['humidity'], data['weather'][0]['description']))
    conn.commit()

def analyze_weather_data(conn):
    """Analyze weather data stored in the SQLite database."""
    cursor = conn.cursor()
    cursor.execute('SELECT AVG(temperature), AVG(humidity) FROM weather')
    result = cursor.fetchone()
    avg_temperature = result[0]
    avg_humidity = result[1]
    print(f"Average Temperature: {avg_temperature}°C")
    print(f"Average Humidity: {avg_humidity}%")

def main():
    # Connect to SQLite database
    conn = sqlite3.connect('weather_data.db')

    # Create weather table if not exists
    create_weather_table(conn)

    # Store weather data retrieved from API
    # Assume 'weather_data' contains the retrieved data
    # Replace this with actual weather data retrieval code
    weather_data = {
        'name': 'New York',
        'main': {'temp': 22.5, 'humidity': 65},
        'weather': [{'description': 'Clear'}]
    }
    store_weather_data(conn, weather_data)

    # Analyze weather data
    analyze_weather_data(conn)

    # Close database connection
    conn.close()

if __name__ == "__main__":
    main()
