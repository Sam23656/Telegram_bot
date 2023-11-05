from aiogram import types, Router, F

from Python_Sql_Requests import get_all_brands

brands_router = Router()


@brands_router.message(F.text == 'Все бренды')
async def all_brands(message: types.Message):
    await message.answer(f"Brands: \n{get_all_brands()}")
