from aiogram.types import WebAppInfo
from aiogram import types

web_app = WebAppInfo(url='https://2492246-yo82697.twc1.net/catalog')

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='Catalog', web_app=web_app)]
    ],
    resize_keyboard=True
)