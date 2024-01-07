import webbrowser
import telebot
from telebot import types
from PIL import Image
bot = telebot.TeleBot('6959262170:AAFZYR7aJG5sI2j2NfD44F9VNqc5gzsoH4Q')
@bot.message_handler(commands=['help', 'info'])
def start(message):
    bot.send_message(message.chat.id, f'<em>Витрина на оформлении 😁</em>', parse_mode='html')
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://github.com/Maxxx-VS?tab=repositorie')
@bot.message_handler(commands=['start', 'main', 'hello'])
def start(message):
    bot.send_message(message.chat.id, f'Привет 👋🏻, {message.from_user.first_name}!')
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, загрузи сюда фотографию\n'
                                      f'или сделай селфи:')
@bot.message_handler(content_types=['photo', 'document'])
def get_photo(message):
    global src
    try:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id) # загружаем фотографию
        downloaded_file = bot.download_file(file_info.file_path)
        #downloaded_file = bot.download_file('C:/Users/hot-z/pythonProject_Bot/photos/file_123.jpg')
        src = './photos/' + file_info.file_path.replace('photos/', '')
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
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
    bot.reply_to(message, f"<b>ВЫБЕРИ ОДИН ФИЛЬТР:\n"
                          f"и немного подожди...</b>", reply_markup=markup, parse_mode='html')
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
    bot.send_photo(callback.from_user.id, img) # возвращает фото с фильтром в чат
    bot.send_message(callback.message.chat.id, f"<b>ЗАГРУЖАЙ ЕЩЁ:</b>", parse_mode='html')

def DarkFilter(r: int, g: int, b: int) -> tuple[int, int, int]:
    result = []
    for color in (r, g, b):
        result = [int(r/3), int(g/3), int(b/3)]
    return tuple(result)
def BrightFilter(r: int, g: int, b: int) -> tuple[int, int, int]:
    result = []
    for color in (r, g, b):
        result = [int(r*3), int(g*3), int(b*3)]
    return tuple(result)
def RedFilter(r: int, g: int, b: int) -> tuple[int, int, int]:
    result = []
    for color in (r, g, b):
        result = [int(r*3), int(g*1), int(b*1)]
    return tuple(result)
def GreenFilter(r: int, g: int, b: int) -> tuple[int, int, int]:
    result = []
    for color in (r, g, b):
        result = [int(r*1), int(g*3), int(b*1)]
    return tuple(result)
def BlueFilter(r: int, g: int, b: int) -> tuple[int, int, int]:
    result = []
    for color in (r, g, b):
        result = [int(r*1), int(g*1), int(b*3)]
    return tuple(result)

img = Image.open("C:/Users/hot-z/pythonProject_Bot/get.jpeg").convert('RGB')
width, height = img.size
print(img.width)
print(img.height)

def apply_filter(img: Image.Image, filt) -> Image.Image:
    for i in range(img.width):
        for j in range(img.height):
            r,g,b = img.getpixel((i, j))
            new_pixel = filt(r,g,b)
            img.putpixel((i, j), new_pixel)
    img.save("C:/Users/hot-z/pythonProject_Bot/photos/processing_photo_on.jpeg")
    return img

bot.polling(non_stop=True)











