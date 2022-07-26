import datetime
import psycopg2
import database
import pandas as pd


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
    def get_latest_reading(cls):
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

    @classmethod
    def get_daily_summary(cls):
        # compute current date
        today = datetime.datetime.today()
        date = today.strftime("%Y-%m-%d %H:%M:%S").split(" ")[0]

        query = "SELECT * FROM iot_temperature WHERE date >= (%s)"

        connection = database.create_connection()

        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (date,))
                result = cursor.fetchall()

        if result is not None:
            # convert result set to pandas dataframe
            df = pd.DataFrame(result,
                              columns=['id',
                                       'date',
                                       'temp_celsius',
                                       'temp_fahrenheit',
                                       'humidity',
                                       'location']
                              )

            # grab the summaries of interest
            summary_df = df.describe()
            summaries = {"temp_celsius": summary_df["temp_celsius"].to_dict(),
                         "temp_fahrenheit": summary_df["temp_fahrenheit"].to_dict(),
                         "humidity": summary_df["humidity"].to_dict()
                         }

            return summaries
        return None
