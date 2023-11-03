import asyncio
import logging
import os

from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

from Python_Sql_Requests.get_all_products import get_all_products

load_dotenv()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.environ.get("BOT_TOKEN_CODE"))
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"{message.chat.id} - {message.from_user.id} - Hello")


@dp.message(Command("AllProducts"))
async def cmd_start(message: types.Message):
    await message.answer(f"Products: \n{get_all_products()}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
