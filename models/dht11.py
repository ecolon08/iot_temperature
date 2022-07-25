import psycopg2
import database


class Dht11Model:
    def __init__(self, id, date, temp_celsius, temp_fahrenheit, humidity, location):
        self._id = id
        self.date = date
        self.temp_celsius = temp_celsius
        self.temp_fahrenheit = temp_fahrenheit
        self.humidity = humidity
        self.location = location

    def json(self):
        return {"id": self._id,
                "date": self.date.strftime("%Y-%m-%d %H:%M:%S"),
                "temp_celsius": self.temp_celsius,
                "temp_fahrenheit": self.temp_fahrenheit,
                "humidity": self.humidity,
                "location": self.location}

    @classmethod
    def find_latest_reading(cls):
        query = "SELECT * FROM iot_temperature ORDER BY date DESC LIMIT 1"

        connection = database.create_connection()

        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()

        if result is not None:
            dht11 = cls(*result)

        connection.close()

        return dht11

