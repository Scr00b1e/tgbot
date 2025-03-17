from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Hi, \nyour name is {message.from_user.first_name}',
                         reply_markup=await kb.inline_cars())

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Do you need help?')

@router.message(F.text == 'what')
async def reply(message: Message):
    await message.answer('Its good')