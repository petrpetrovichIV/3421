import sqlite3
import datetime
import requests

connection = sqlite3.connect("db.sl3")
cursor = connection.cursor()

# cursor.execute("""
#     create table weather_cities (
#         ID integer PRIMARY KEY,
#         city text,
#         temp real,
#         feels_like real,
#         humidity integer,
#         date_time text
#     );
# """)
# connection.commit()
key = '2516d7b16bddecafc54e491f03da8399'
city = input("city: ")
city_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric').json()

city_name = city_weather["name"]
temp = city_weather["main"]["temp"]
feels_like = city_weather["main"]["feels_like"]
humidity = city_weather["main"]["humidity"]

cursor.execute(f"""
    insert into weather_cities
        (city, temp, feels_like, humidity, date_time) values
        ('{city_name}', {temp}, {feels_like}, {humidity}, '{datetime.datetime.now()}');
""")
connection.commit()


cursor.execute("select * from weather_cities;")
connection.commit()
cities = cursor.fetchall()
for city in cities:
    print(city)

connection.close()