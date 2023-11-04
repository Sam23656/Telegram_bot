from aiogram import types, Router, F

from Python_Sql_Requests import get_all_categories

categories_router = Router()


@categories_router.message(F.text == 'Все категории')
async def all_categories(message: types.Message):
    await message.answer(f"Categories: \n{get_all_categories()}")

