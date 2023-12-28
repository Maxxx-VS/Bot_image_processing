import telebot
import sqlite3
bot = telebot.TeleBot('6959262170:AAFZYR7aJG5sI2j2NfD44F9VNqc5gzsoH4Q')

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('database_photo.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50)')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет! Как тебя зовут?')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    pass





bot.polling(non_stop=True)