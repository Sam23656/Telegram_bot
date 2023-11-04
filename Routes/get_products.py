from aiogram import types, Router
from aiogram.filters import Command

from Python_Sql_Requests import get_all_products, get_five_last_products

products_router = Router()


@products_router.message(Command(commands=['AllProducts']))
async def cmd_start(message: types.Message):
    await message.answer(f"Products: \n{get_all_products()}")


@products_router.message(Command(commands=['Last5Products']))
async def cmd_start(message: types.Message):
    await message.answer(f"Products: \n{get_five_last_products()}")
