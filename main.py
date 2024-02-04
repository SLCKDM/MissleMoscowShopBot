"""Входная точка"""
import asyncio
import logging
from aiogram import Bot, Dispatcher

BOT_TOKEN = '6574504495:AAFD7HI5zsqDcPlD7w9lwkJGtDnLe03ZjF8'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)


async def main():
    from handlers import dp
    try:
        await dp.start_polling()
    finally:
        if bot.session:
            await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')
