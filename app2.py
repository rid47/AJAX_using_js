import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template('index2.html')


@app.route('/get_weather', methods=["POST"])
def get_weather():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    city = request.form.get("mycity")
    print(f"City searched for {city}")
    params = {
        "q": city,
        "appid": 'fe8717ffdd49f4a6c4c3a165b90cbe29'
    }
    response = requests.get(url, params).json()
    # print(f"response: {response['cod']} and type {type(response['cod'])}")
    if response['cod'] != 200:
        return jsonify({"success": False})

    else:
        weather = {

            'success': True,
            'city': response['name'],
            'temperature': round((response['main']['temp'] - 273.15), 2),
            'description': response['weather'][0]['description'],

            }
        return jsonify(weather)


if __name__ == "__main__":
    app.run(debug=True)
