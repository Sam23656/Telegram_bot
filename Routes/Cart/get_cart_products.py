from aiogram import Router, types, F

from Python_Sql_Requests import get_cart_products
from Python_Sql_Requests.Clients.get_client_cart_id import get_client_cart_id
from Utils import get_chat_id

get_cart_products_router = Router()


@get_cart_products_router.message(F.text == 'Корзина')
async def all_products(message: types.Message):
    await message.answer(f"Products: \n{get_cart_products(get_client_cart_id(get_chat_id(message)))}")
