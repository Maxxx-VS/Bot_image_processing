import telebot
import requests
import json
bot = telebot.TeleBot('6959262170:AAFZYR7aJG5sI2j2NfD44F9VNqc5gzsoH4Q')
API = '88e1d9b53f2f324d6004ee7e57cf40cc'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Напиши название города")


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        #bot.reply_to(message, f'Сечас погода: {res.json()}')
        bot.reply_to(message, f'Сечас погода: {temp}')
        image = 'weather_2.png' if temp > 10.0 else 'weather_3.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, "Такого города не существует")








bot.polling(non_stop=True)