import requests
import telebot

token = '2052616546:AAHcWxtiGz8WvSUY9uQfo7R0nWV-YwEhCAE'
key = '2516d7b16bddecafc54e491f03da8399'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "City name: ")

@bot.message_handler(content_types=['text'])
def weather(message):
    city = message.text.lower()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'
    data = requests.get(url).json()

    text = f'''Now in city {city.capitalize()}:\n
                {data["weather"][0]["main"]}\n
                {data["weather"][0]["description"]}\n
                {data["main"]["temp"]}° ({data["main"]["feels_like"]}°)\n
                {data["main"]["humidity"]}%\n
                {data["wind"]["speed"]} m/s
            '''
    bot.reply_to(message, text)

bot.polling(none_stop=True)