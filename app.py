from flask import Flask, render_template, request
import requests
from config import API_KEY, BASE_URL
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    params = {
        'key': API_KEY,
        'q': city
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200 and "current" in data:
        weather_data = {
            'city': data['location']['name'],
            'country': data['location']['country'],
            'temp_c': data['current']['temp_c'],
            'condition': data['current']['condition']['text'],
            'icon': data['current']['condition']['icon']
        }
        return render_template('result.html', weather=weather_data)
    else:
        error_msg = data.get("error", {}).get("message", "City not found.")
        return render_template('index.html', error=error_msg)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

