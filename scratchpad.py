import datetime
import database
import numpy as np
import pandas as pd


today = datetime.datetime.today()
date = today.strftime("%Y-%m-%d %H:%M:%S").split(" ")[0]

# query = f"SELECT * FROM iot_temperature WHERE date >= \'{date}\'"
query = f"SELECT * FROM iot_temperature WHERE date >= (%s)"

connection = database.create_connection()

with connection:
    # df = pd.read_sql_query(query, connection, parse_dates)
    with connection.cursor() as cursor:
        cursor.execute(query, (date,))
        result = cursor.fetchall()

    # convert to pandas dataframe
    df = pd.DataFrame(result, columns=['id', 'date', 'temp_celsius', 'temp_fahrenheit', 'humidity', 'location'])

    # grab the summaries of interest
    summary_df = df.describe()
    summaries = {"temp_celsius": summary_df["temp_celsius"].to_dict(),
                 "temp_fahrenheit": summary_df["temp_fahrenheit"].to_dict(),
                 "humidity": summary_df["humidity"].to_dict()
                 }

# print(type(result))
# print(result[0])
# print(len(result))
# df = pd.DataFrame(result, columns=['id', 'date', 'temp_celsius', 'temp_fahrenheit', 'humidity', 'location'])
# print(df.head())
# print(df.describe())
# print(df.describe()['temp_celsius'].to_dict())
print(summaries)
print(type(summary_df["temp_celsius"]))
