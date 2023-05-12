import requests
import datetime

# Set the latitude and longitude of your location.
MY_LAT = 51.507351
MY_LNG = -0.127758

# Define parameters for the API request.
parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0,
}

# Make a request to the sunrise-sunset API.
response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

# Extract sunrise and sunset times from the API response.
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

# Print the sunrise and sunset times.
print(sunrise)
print(sunset)

# Get the current time.
now = datetime.datetime.now()
print(now.hour)
