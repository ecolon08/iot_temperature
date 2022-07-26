from flask import Flask
from flask_restful import Api
from resources.living_room import Dht11, SensorDailySummary


def celsius_to_fahrenheit(celsius):
    return (celsius * (9/5)) + 32


# Define the app
app = Flask(__name__)
api = Api(app)

api.add_resource(Dht11, '/dht11/livingroom')
api.add_resource(SensorDailySummary, '/dht11/livingroom/summary')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
