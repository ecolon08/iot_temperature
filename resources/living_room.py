from flask_restful import Resource
from models.dht11 import Dht11Model


class Dht11(Resource):
    def get(self):
        dht11 = Dht11Model.find_latest_reading()
        if dht11:
            return dht11.json()
        return {"message": "failed to get reading"}, 404
