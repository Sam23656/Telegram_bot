from aiogram import types, Router, F

from Python_Sql_Requests import get_order_statistic
from Utils import get_chat_id

order_router = Router()


@order_router.message(F.text == 'Все заказы')
async def all_categories(message: types.Message):
    await message.answer(f"Orders: \n{get_order_statistic(get_chat_id(message))}")
