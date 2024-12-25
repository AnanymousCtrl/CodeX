from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_key = '' #your api key here
@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city").strip()
        url = "http://api.openweathermap.org/data/2.5/weather"
        # complete_url = url + "?q=" + city + "&appid=" + api_key
        params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            weather_data = {
                "city" : data["name"],
                "country_name" : data["sys"]["country"],
                "temp" : data["main"]["temp"],
                "feels_like" : data["main"]["feels_like"],
                "humidity" : data["main"]["humidity"],
                "condition" : data["weather"][0]["description"],
                "wind_speed" : data["wind"]["speed"]
            }
        
        except:
            error_message = "ERROR!!"

    return render_template("index.html", weather=weather_data, error=error_message)
    
if __name__ == "__main__":
    app.run(debug=True)