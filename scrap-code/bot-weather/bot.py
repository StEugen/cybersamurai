import telebot
from dotenv import load_dotenv
load_dotenv()
import os
import pyowm
import pyowm.exceptions 


WEATHER_TOKEN=os.getenv('WEATHER_TOKEN')
owm = pyowm.OWM(WEATHER_TOKEN)
TOKEN=os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Hello')

@bot.message_handler(commands=['weather'])
def weather(message):
    sent = bot.send_message(message.chat.id, "Enter the city: ")
    bot.register_next_step_handler(sent, send_forecast)

def send_forecast(message):
    try:
        get_forecast(message.text)
    except pyowm.exceptions.api_response_error.NotFoundError:
        bot.send_message(message.chat.id, "Wrong place")
    forecast = get_forecast(message.text)
    bot.send_message(message.chat.id, forecast)


def get_forecast(place):
	observation = owm.weather_at_place(place)
	weather = observation.get_weather()
	temperature = weather.get_temperature('celsius')["temp"]
	clouds = weather.get_clouds()
	humidity = weather.get_humidity()
	forecast = f" In {place} is currently {weather.get_detailed_status()}\n Temperature = {temperature} Celsius\n Clouds probability = {clouds}%\n Humidity is {humidity}%"
	return forecast

bot.infinity_polling()