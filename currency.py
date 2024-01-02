# from currency_converter import CurrencyConverter
# import telebot
# from telebot import types
#
# bot = telebot.TeleBot('6959262170:AAFZYR7aJG5sI2j2NfD44F9VNqc5gzsoH4Q')
# currency = CurrencyConverter()
# amount = 0
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "Введите сумму для конвертации:")
#     bot.register_next_step_handler(message, summa)
#
# def summa(message):
#     global amount
#     try:
#         amount = int(message.text.strip())
#     except ValueError:
#         bot.send_message(message.chat.id, 'Неверный формат. Введите сумму:')
#         bot.register_next_step_handler(message, summa)
#         return
#
#     if amount > 0:
#         markup = types.InlineKeyboardMarkup(row_width=2)
#         btn_1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
#         btn_2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
#         btn_3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
#         btn_4 = types.InlineKeyboardButton('ДРУГОЕ', callback_data='else')
#         markup.add(btn_1, btn_2, btn_3, btn_4)
#         bot.send_message(message.chat.id, 'Выбирай пару для конвертации', reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, 'Недопустимая велечина. Введите другую сумму:')
#         bot.register_next_step_handler(message, summa)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data != 'else':
#         values = call.data.upper().split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(call.message.chat.id, f'Результат: {round(res, 2)}. Введи новую сумму:')
#         bot.register_next_step_handler(call.message, summa)
#     else:
#         bot.send_message(call.message.chat.id, 'Введите пару значений через "/"')
#         bot.register_next_step_handler(call.message, my_currency)
#
# def my_currency(message):
#     try:
#         values = message.text.upper().split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(message.chat.id, f'Результат: {round(res, 2)}. Введи новую сумму:')
#         bot.register_next_step_handler(message, summa)
#     except Exception:
#         bot.send_message(message.chat.id, f'Некорректный ввод. Попробуй ещё раз!')
#         bot.register_next_step_handler(message, summa)
#
# bot.polling(non_stop=True)