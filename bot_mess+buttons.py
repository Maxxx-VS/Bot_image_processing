import webbrowser
import telebot
from telebot import types
from PIL import Image
from filters import DarkFilter, BrightFilter, RedFilter, GreenFilter, BlueFilter, apply_filter
bot = telebot.TeleBot('6959262170:AAFZYR7aJG5sI2j2NfD44F9VNqc5gzsoH4Q')
# new_file = None
@bot.message_handler(commands=['help', 'info'])
def start(message):
    bot.send_message(message.chat.id, f'<em>Витрина на оформлении 😁</em>', parse_mode='html')
@bot.message_handler(commands=['start', 'main', 'hello'])
def start(message):
    bot.send_message(message.chat.id, f'Привет 👋🏻, {message.from_user.first_name}!')
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, загрузи сюда фотографию\n'
                                      f'или сделай селфи:')
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    global new_file
    global src
    try:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id) # загружаем фотографию
        downloaded_file = bot.download_file(file_info.file_path)
        src = './photos/' + file_info.file_path.replace('photos/', '')
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
            #new_file.close()
    except Exception as e:
        bot.reply_to(message, e)
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton('Темный фильтр', callback_data='dark_filter')
    btn_2 = types.InlineKeyboardButton('Светлый фильтр', callback_data='light_filter')
    btn_3 = types.InlineKeyboardButton('Красный фильтр', callback_data='red_filter')
    btn_4 = types.InlineKeyboardButton('Зеленый фильтр', callback_data='green_filter')
    btn_5 = types.InlineKeyboardButton('Синий фильтр', callback_data='blue_filter')
    btn_6 = types.InlineKeyboardButton("Developer's Git", url='https://github.com/Maxxx-VS?tab=repositorie')
    markup.row(btn_1, btn_2)
    markup.row(btn_3, btn_4, btn_5)
    markup.row(btn_6)
    bot.reply_to(message, f"<b>ВЫБЕРИ ОДИН ФИЛЬТР:</b>", reply_markup=markup, parse_mode='html')
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'dark_filter':
        filt = DarkFilter
    elif callback.data == 'light_filter':
        filt = BrightFilter
    elif callback.data == 'red_filter':
        filt = RedFilter
    elif callback.data == 'green_filter':
        filt = GreenFilter
    else:
        filt = BlueFilter
    def processing():
        global img
        img = Image.open(src).convert('RGB')
        img = apply_filter(img, filt)
        img.show()
    processing()
    bot.send_photo(callback.from_user.id, img)
    bot.send_message(callback.message.chat.id, f"<b>ЗАГРУЖАЙ ЕЩЁ:</b>", parse_mode='html')
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://github.com/Maxxx-VS?tab=repositorie')

bot.polling(non_stop=True)







# def on_click(message):
#
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

#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')



