from aiogram.types import WebAppInfo
from aiogram import types

web_app = WebAppInfo(url='https://ya.ru')

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='Catalog', web_app=web_app)]
    ],
    resize_keyboard=True
)