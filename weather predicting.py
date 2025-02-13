import requests

def get_weather(latitude, longitude):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'
    response = requests.get(url)
    return response.json()

def book_flight_and_get_weather(departure_city_coords, destination_city_coords):
    departure_weather = get_weather(departure_city_coords['latitude'], departure_city_coords['longitude'])
    destination_weather = get_weather(destination_city_coords['latitude'], destination_city_coords['longitude'])
    
    def book_flight(departure, destination):
        return f"Flight booked from {departure} to {destination}."
    
    departure_weather_info = f"Weather in departure city: {departure_weather['current_weather']['weathercode']}, Temp: {departure_weather['current_weather']['temperature']}°C"
    destination_weather_info = f"Weather in destination city: {destination_weather['current_weather']['weathercode']}, Temp: {destination_weather['current_weather']['temperature']}°C"
    
    booking_confirmation = book_flight('Departure City', 'Destination City')
    
    return f"{booking_confirmation}\n\n{departure_weather_info}\n\n{destination_weather_info}"

departure_city_coords = {"latitude": 13.0827, "longitude": 80.2707 }  # Chennai
destination_city_coords = {"latitude": 51.5074, "longitude": -0.1278}  # London
print(book_flight_and_get_weather(departure_city_coords, destination_city_coords))
