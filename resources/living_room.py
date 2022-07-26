from flask_restful import Resource
from models.dht11 import Dht11Model


class Dht11(Resource):
    def get(self):
        dht11 = Dht11Model.get_latest_reading()
        if dht11:
            return dht11.json()
        return {"message": "failed to get reading"}, 404


class SensorDailySummary(Resource):
    def get(self):
        summary = Dht11Model.get_daily_summary()
        if summary is not None:
            return summary
        return {"message": "Failed to load summary. Database read error"}, 500
