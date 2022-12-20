from telebot import types 
import re

with open('dates.txt', 'r') as f:
    dates = [line.strip() for line in f]

keyboard = types.InlineKeyboardMarkup()
for item in dates:
    buttons = [
        types.InlineKeyboardButton(text=f'{item}', callback_data="dates")
    ]
    keyboard.add(*buttons)



