import telebot
from config import BOT_API_TOKEN
from telebot import types
from workjson import get_json, take_info, teacher_json
from dates import *
global sname 

bot = telebot.TeleBot(BOT_API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.reply_to(message, 'Enter you surname: ')
    bot.register_next_step_handler(msg, dates)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Help displayed')

def dates(message):
    global sname  
    sname = message.text
    msg = bot.reply_to(message, "Choose week", reply_markup=keyboard)
    bot.register_next_step_handler(msg, test)

def test(message):
    week = message.text
    teacher_json(sname, week)
    get_json()
    msg = take_info()
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda messages: True)
def any_message(message):
    msg = "Cannot understand you. Please, enter '/help' or '/start' "
    bot.reply_to(message, msg)

if __name__ == "__main__":
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()
    bot.infinity_polling()