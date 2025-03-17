import telebot
from telebot import types
from currency_converter import CurrencyConverter 
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Convert currency')
    bot.register_next_step_handler(message, summa)
    
def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Text number')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Other', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Choose currency', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Must be more than 0")
        bot.register_next_step_handler(message, summa)
    
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Becomes: {res}. You can convert again')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Write some values with slash')
        bot.register_next_step_handler(call.message, mycurrency)

def mycurrency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Becomes: {round(res, 2)}. You can convert again')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Write correct value')
        bot.register_next_step_handler(message, summa)   


bot.polling(non_stop=True)