from aiogram import Bot, Dispatcher, types, executor
from aiohttp import web 
from config import BOT_API_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token=BOT_API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(text='Choose a day')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
