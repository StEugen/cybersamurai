import telebot
from telebot import types
from dotenv import load_dotenv
load_dotenv()
import os


TOKEN=os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Hello')

            
bot.infinity_polling()