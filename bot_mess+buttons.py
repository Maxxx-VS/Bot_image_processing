# import telebot
# import webbrowser
# from telebot import types
# bot = telebot.TeleBot('6959262170:AAFZYR7aJG5sI2j2NfD44F9VNqc5gzsoH4Q')
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn_1 = types.KeyboardButton('GIT разработчика')
#     markup.row(btn_1)
#     btn_2 = types.KeyboardButton('Удалить фото')
#     btn_3 = types.KeyboardButton('Изменить текст')
#     markup.row(btn_2, btn_3)
#     # bot.reply_to(message, 'Фото загружено')
#
#     file = open('4.Quali-sono-i-migliori-bot-di-Telegram.jpg', 'rb')
#     bot.send_photo(message.chat.id, file, reply_markup=markup)
#     # bot.send_audio(message.chat.id, file, reply_markup=markup)
#     # bot.send_video(message.chat.id, file, reply_markup=markup)
#     # bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
#
#     bot.register_next_step_handler(message, on_click)
#
# def on_click(message):
#     if message.text == "GIT разработчика":
#         bot.send_message(message.chat.id, 'GIT открыт')
#     elif message.text == "Удалить фото":
#         bot.send_message(message.chat.id, 'Фото удалено')
#
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn_1 = types.InlineKeyboardButton('GIT разработчика', url='https://github.com/Maxxx-VS?tab=repositorie')
#     markup.row(btn_1)
#     btn_2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
#     btn_3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
#     markup.row(btn_2, btn_3)
#     bot.reply_to(message, 'Фото загружено', reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)
#
#
# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://github.com/Maxxx-VS?tab=repositorie')
#
# @bot.message_handler(commands=['start', 'main', 'hello'])
# def main(message):
#     bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
#
# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, '<b>Help</b> <em><u>inform</u></em>', parse_mode='html')
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')
#
# bot.polling(non_stop=True)