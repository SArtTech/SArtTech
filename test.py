#import telepot;
import telebot;
from telebot import types;
import random;

TOKEN = "2074671002:AAESx8OSWY2PlRXzRTzkZRNq_chT_ee6oBY"
bot = telebot.TeleBot(TOKEN)
#bot.remove_webhook()

@bot.message_handler(commands=['start'])

def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Привет")
    but2 = types.KeyboardButton("Позвоните мне")
    markup.add(but1,but2)
    bot.send_message(message.chat.id,"Здравствуйте, " + message.chat.first_name + "\nСпасибо, что обратились в нашу компанию!", reply_markup=markup)
    #bot.reply_to(message,"Здравствуйте, {message.chat.first_name}\nСпасибо, что обратились в нашу компанию!", parse_mode='html', reply_markup=markup)
    return(message.chat.id)

@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.chat.type == 'private':
        if message.text == "Привет":
            bot.send_message(message.chat.id, "Привет, "+ message.chat.first_name)

        elif message.text == "Позвоните мне":
            bot.send_message(message.chat.id, "Позвоним, "+ message.chat.first_name)
if __name__ == '__main__':
    bot.polling(none_stop=True)

""" URL = "https://api.telegram.org/bot%s/" % BOT_TOKEN
MyURL = "https://example.com/hook"

api = requests.Session()
application = tornado.web.Application([
    (r"/", Handler),
])

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, signal_term_handler)
    try:
        set_hook = api.get(URL + "setWebhook?url=%s" % MyURL)
        if set_hook.status_code != 200:
            logging.error("Can't set hook: %s. Quit." % set_hook.text)
            exit(1)
        application.listen(8888)
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        signal_term_handler(signal.SIGTERM, None) """