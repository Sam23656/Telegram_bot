import re

from aiogram import Router, types, F

from Python_Sql_Requests import add_product_to_cart, get_client_cart_id, get_product_id_by_name

from Utils import get_chat_id

add_product_to_cart_router = Router()


@add_product_to_cart_router.message(F.text.startswith('Добавить'))
async def add_product_to_cart_f(message: types.Message):
    match = re.match(r'^Добавить\s+\'(.*?)\'', message.text)
    if match:
        product_name = match.group(1)
        await message.answer(add_product_to_cart(get_client_cart_id(get_chat_id(message)),
                                                 get_product_id_by_name(product_name), 1))
    else:
        await message.answer('Неверный ввод')
