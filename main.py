import telebot
import webbrowser

bot = telebot.TeleBot('8120813282:AAEZAZlQz_YhK7yY96hjWRX-GNIn2LYGC2Q')

#@bot.message_handler(commands=['site', 'website'])
#def site(message):
#   webbrowser.open('https://itproger.com') 

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Hi, {message.from_user.username} !')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Help information', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
      bot.send_message(message.chat.id, f'Hi, {message.from_user.username} !')  
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(non_stop=True)
