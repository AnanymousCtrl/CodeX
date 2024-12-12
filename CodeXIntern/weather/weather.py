import requests
import flask
print("Weather Dashboard")

api_key  = "42995734c58d48200de22715d65f80fd"

base_url = "http://api.openweathermap.org/data/2.5/weather"

while True:
    city= input("Enter City Name:(exit for quit) ").strip()
    if city.lower() == "exit":
        break
    if not city:
        print("City name cannot be empty")

    complete_url = base_url + "?q=" + city + "&appid=" + api_key

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        # print(data)
        country_name = data["sys"].get('country')
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        print(f'Weather In {city}, {country_name}')    
        print(f"Country: ", country_name)
        print(f"Temperature:{temp}deg C")
        print(f"Feels Like:{feels_like}deg C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed}m/s")
        print(f"Condition: ", condition)



    except:
        print("Error")

# print(response.json())

