import telebot
from config import BOT_API_TOKEN
from telebot import types
from test_json import get_json, take_info, teacher_json
from dates import *


bot = telebot.TeleBot(BOT_API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.reply_to(message, 'Choose a week', reply_markup=keyboard)
    bot.register_next_step_handler(msg, dates)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Help displayed')


def dates(message):
    sname = '' 
    week = message.text
    teacher_json(sname, week)
    get_json()
    msg = take_info()
    bot.send_message(message.chat.id, msg)


if __name__ == "__main__":
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()
    bot.infinity_polling()