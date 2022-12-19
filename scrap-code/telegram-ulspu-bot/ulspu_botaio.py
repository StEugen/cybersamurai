from aiogram import Bot, Dispatcher, types, executor
from aiohttp import web 
from config import BOT_API_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, italic, code
from aiogram.types import ParseMode
from test_json import get_json


bot = Bot(token=BOT_API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)



@dp.message_handler(commands="help")
async def help(message:types.Message):
    await message.answer(text='Help displayed')

@dp.message_handler(commands="start")
async def start(msg: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(text="15-16 weeks", callback_data="test")
    ]
    keyboard.add(*buttons)
    await msg.answer(text='Choose a week', reply_markup=keyboard)




@dp.callback_query_handler(text="test")
async def test(call: types.CallbackQuery):
    text = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-15.json'
    msg = get_json(text)
    await bot.send_message(call.from_user.id, text=msg)


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_msg(msg: types.Message):
    message_text = text(('Я не знаю, что с этим делать:'), italic('\n Есть команда: '), code('/help'))
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
