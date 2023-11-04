import asyncio
import logging
import os

from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

from Routes import products_router, categories_router, brands_router

load_dotenv()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.environ.get("BOT_TOKEN_CODE"))
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"{message.chat.id} - {message.from_user.id} - Hello")


async def main():
    dp.include_router(products_router)
    dp.include_router(categories_router)
    dp.include_router(brands_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
