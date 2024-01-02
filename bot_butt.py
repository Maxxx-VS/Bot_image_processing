# from aiogram import Bot, Dispatcher, types, executor
#
# bot = Bot('6959262170:AAFZYR7aJG5sI2j2NfD44F9VNqc5gzsoH4Q')
# dp = Dispatcher(bot)
#
# @dp.message_handler(content_types=['photo']) # commands=['start']   content_types=['text']
# async def start(message: types.Message):
#     # await bot.send_message(message.chat.id, 'Привет!')
#     # await message.answer('Привет')
#     await message.reply('Привет!')
#     # file = open('/some.png', 'rb')
#     # await message.answer_photo(file)
#
#
# @dp.message_handler(commands=['inline'])
# async def info(message: types.Message):
#     markup = types.InlineKeyboardMarkup() # row_widht=2
#     markup.add(types.InlineKeyboardButton("Developer's Git", url='https://github.com/Maxxx-VS?tab=repositorie'))
#     markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
#     await message.reply('Hello', reply_markup=markup)
#
#
# @dp.callback_query_handler()
# async def callback(call):
#     await call.message.answer(call.data)
#
#
# @dp.message_handler(commands=['reply'])
# async def reply(message: types.Message):
#     markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
#     markup.add(types.KeyboardButton('Site'))
#     markup.add(types.KeyboardButton('Website'))
#     await message.answer('Hello', reply_markup=markup)
#
#
#
#
#
# executor.start_polling(dp)