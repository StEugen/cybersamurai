import telebot
from dotenv import load_dotenv
load_dotenv()
import os
from telebot import types
import config 
import requests


token=os.getenv('BOT_TOKEN')
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Hello')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Start")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Start":
        bot.send_message(message.chat.id,"Hello")


def get_page(group, week=''):
    if week:
        week = str(week) + '/'
    url = '{domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        domain=config.domain, 
        week=week, 
        group=group)
    response = requests.get(url)
    web_page = response.text
    return web_page
        
bot.infinity_polling()