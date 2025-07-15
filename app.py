from flask import Flask, render_template, request, jsonify
import requests
import os

from config import API_KEY, BASE_URL

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.json.get('city')
    if not city:
        return jsonify({"error": "City is required"}), 400

    params = {"key": API_KEY, "q": city}
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if "error" in data:
            return jsonify({"error": data["error"]["message"]}), 404

        weather_data = {
            "location": data["location"]["name"],
            "temperature": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"],
            "icon": "http:" + data["current"]["condition"]["icon"],
            "humidity": data["current"]["humidity"],
            "wind": data["current"]["wind_kph"]
        }
        return jsonify(weather_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)

