import telebot
import requests

token = '8294006330:AAFp_umVb_NqZ_xgioqz7xfEP3PjWwhqQVg'

API = '2516d7b16bddecafc54e491f03da8399'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "City name: ")

@bot.message_handler(content_types=['text'])
def weather(message):
    city = message.text.lower()
    city_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric').json()

    temp = city_weather["main"]["temp"]
    desc = city_weather["weather"][0]["description"]


    bot.reply_to(message, f'Now in the {city.upper()} {temp}° \n{desc} ')

bot.polling(none_stop=True)