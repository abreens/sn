from flask import Flask, render_template
import requests
import os

try:
    import openweathermap  # only needed for localhost, that's why it's in the try/except statement
except ImportError as e:
    pass


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    query = "Essen,BE"
    unit = "metric"  # use "imperial" for Fahrenheit

    api_key = os.environ.get("OWM_API_KEY")

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}".format(query, unit, api_key)
    data = requests.get(url=url)  # GET request to the OpenWeatherMap API

    return render_template("index.html", data=data.json())


if __name__ == '__main__':
    app.run(debug=True)