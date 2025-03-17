import asyncio
import logging

from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Bot, Dispatcher

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hi')

async def main():
    await bot.delete_webhook()

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')