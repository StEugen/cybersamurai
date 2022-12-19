import telebot
from config import BOT_API_TOKEN
from telebot import types
from test_json import get_json, take_info
from dates import *


bot = telebot.TeleBot(BOT_API_TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
    #keyboard = types.InlineKeyboardMarkup()
    #buttons = [
    #    types.InlineKeyboardButton(text='', callback_data="dates1"),
    #   types.InlineKeyboardButton(text='', callback_data="dates2")
    #]
    #keyboard.add(*buttons)
    bot.send_message(message.chat.id, 'Choose a week', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Help displayed')

#@bot.callback_query_handler(lambda query: query.data == 'dates')
@bot.callback_query_handler(func=lambda query: True)
def dates(query):
    #text = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-15.json'
    #get_json(text)
    #msg = take_info()
    #bot.send_message(query.message.chat.id, msg)
    
    ### I don't like this shit here ###
    if query.data == "dates1":
        date = 15
        text = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-{date}.json'
        get_json(text)
        msg = take_info()
        bot.send_message(query.message.chat.id, msg)
    if query.data == "dates2":
        date = 17
        text = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-{date}.json'
        get_json(text)
        msg = take_info()
        bot.send_message(query.message.chat.id, msg)



if __name__ == "__main__":
    bot.infinity_polling()