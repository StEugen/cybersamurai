import telebot
from config import BOT_API_TOKEN
from telebot import types
from test_json import get_json, take_info
from dates import *


bot = telebot.TeleBot(BOT_API_TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.reply_to(message, 'Choose a week', reply_markup=keyboard)
    #bot.register_next_step_handler(message, dates, reply_markup=keyboard)
    bot.register_next_step_handler(msg, dates)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Help displayed')



#@bot.callback_query_handler(lambda query: query.data == 'dates')
#@bot.callback_query_handler(func=lambda query: True)
def dates(message): #(query):
    #try:
    #text = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-15.json'
    user_input = message.text
    get_json(user_input)
    #take_date()
    msg = take_info()
    bot.send_message(message.chat.id, msg)
    #except Exception as e:
    #bot.reply_to(message, "ooops")
    ### I don't like this shit here ###


if __name__ == "__main__":
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()
    bot.infinity_polling()