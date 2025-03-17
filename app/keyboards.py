from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Catalog')],
    [KeyboardButton(text='Trash'), KeyboardButton(text='Contacts')]
],  resize_keyboard=True,
    input_field_placeholder='Choose menu options')

settings = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Youtube', url='https://youtube.com')]])

cars = ['Tesla', 'Mercedes', 'BMW', 'Honda']

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url='https://youtube.com'))
    return keyboard.adjust(2).as_markup()