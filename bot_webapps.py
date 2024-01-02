# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types.web_app_info import WebAppInfo
# # https://github.com/Maxxx-VS/Test_html.git
#
# bot = Bot('6959262170:AAFZYR7aJG5sI2j2NfD44F9VNqc5gzsoH4Q')
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     markup = types.ReplyKeyboardMarkup()
#     markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://github.com/Maxxx-VS/Test_html.git')))
#     await message.answer("Привет!!!", reply_markup=markup)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# executor.start_polling(dp)