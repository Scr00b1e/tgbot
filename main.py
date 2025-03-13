import telebot
from telebot import types

bot = telebot.TeleBot('8120813282:AAEZAZlQz_YhK7yY96hjWRX-GNIn2LYGC2Q')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn2 = types.KeyboardButton('Delete photo')
    btn3 = types.KeyboardButton('Edit text')
    markup.row(btn1)
    btn1 = types.KeyboardButton('Enter to site 😁')
    markup.row(btn2, btn3)
    file = open('./diditelluthatimissu.mp3')
    bot.send_audio(message.chat.id, file, reply_markup=markup)
    #file = open('./image.png', 'rb')
    #bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, 'Hi', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Enter to site':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Delete photo':
        bot.send_message(message.chat.id, 'Delete')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    btn2 = types.InlineKeyboardButton('Edit text', callback_data='edit')
    markup.add(types.InlineKeyboardButton('Enter to site', url='https://monkeytype.com/'))
    markup.row(btn1, btn2)
    bot.reply_to(message, 'Such an amazing photo!', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


bot.polling(non_stop=True)