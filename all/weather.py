import requests

key = '2516d7b16bddecafc54e491f03da8399'
city = input('city: ')

city_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric').json()

temp = city_weather["main"]["temp"]
desc = city_weather["weather"][0]["description"]

print(str(temp) + '\n' + desc)