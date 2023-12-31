# import telebot
# import sqlite3
# bot = telebot.TeleBot('6959262170:AAFZYR7aJG5sI2j2NfD44F9VNqc5gzsoH4Q')
# name = None
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('database_photo.sql')
#     cur = conn.cursor()
#
#     cur.execute("CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), password varchar(50))")
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, 'Привет! Как тебя зовут?')
#     bot.register_next_step_handler(message, user_name)
#
# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, f'Отлично, {message.from_user.first_name}, введи пароль!')
#     bot.register_next_step_handler(message, user_password)
#
# def user_password(message):
#     password = message.text.strip()
#     conn = sqlite3.connect('database_photo.sql')
#     cur = conn.cursor()
#
#     cur.execute("INSERT INTO users (name, password) VALUES ('%s', '%s')" % (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
#     bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)
#     # bot.register_next_step_handler(message, user_password)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     conn = sqlite3.connect('database_photo.sql')
#     cur = conn.cursor()
#
#     cur.execute('SELECT * FROM users')
#     users = cur.fetchall() # функция возвращает все записи
#
#     info = ''
#     for i in users:
#         info += f'Имя {i[1]}, пароль: {i[2]}\n'
#
#     cur.close()
#     conn.close()
#
#     bot.send_message(call.message.chat.id, info)
#
#
# bot.polling(non_stop=True)