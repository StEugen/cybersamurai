from telebot import types 
from workjson import get_dates
get_dates()
with open('files/dates', 'r') as f:
    dates = [line.strip() for line in f]

keyboard = types.ReplyKeyboardMarkup(row_width=1)
for item in dates:
    keyboard.add(item)

