import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    if request.method == "POST":
        city = request.form.get("mycity")
        print(f"City searched for {city}")
    else:
        city = "Dhaka"
    params = {
        "q": city,
        "appid": 'fe8717ffdd49f4a6c4c3a165b90cbe29'
    }
    response = requests.get(url, params).json()

    try:
        city = response['name']
        weather = {

            'city': response['name'],
            'temperature': round((response['main']['temp'] - 273.15), 2),
            'description': response['weather'][0]['description'],

            }
    except Exception as e:
        print(e)
        return render_template('error.html', message="City Not Found")

    # print(response)
    # print(weather)

    return render_template('index.html', weather=weather)


if __name__ == "__main__":
    app.run(debug=True)
