import os
import psycopg2
from dotenv import load_dotenv

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS iot_temperature 
(id SERIAL PRIMARY KEY, date TIMESTAMP, temp_celsius FLOAT,
 temp_fahrenheit FLOAT, humidity FLOAT, location VARCHAR(25))
"""

INSERT_ENTRY = """
INSERT INTO iot_temperature (date, temp_celsius, temp_fahrenheit, humidity, location)
VALUES (%s, %s, %s, %s, %s)
"""


def create_connection():
    load_dotenv()
    database_uri = os.environ["DATABASE_URI"]
    try:
        return psycopg2.connect(database_uri)
    except:
        print("Error opening up connection")


def create_table(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TABLE)


def database_setup():
    # create connection
    conn = create_connection()

    # create table
    create_table(conn)


def add_entry(connection, date, temp_celsius, temp_fahrenheit, humidity, location):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_ENTRY, (date, temp_celsius, temp_fahrenheit, humidity, location))


if __name__ == '__main__':
    database_setup()
