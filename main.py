from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

API_TOKEN = '8060956140:AAHcL9KvIsb3ZSK1bnu6XDrQOGo__-0eMq4'

bot = Bot(token = API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    kb = [
        [types.KeyboardButton(text = "98")],
        [types.KeyboardButton(text = "567456")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard = kb)
    await message.reply('Привет \n Бездарь ты \n школота №б"ная',
                        reply_markup = keyboard)

async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())    
    