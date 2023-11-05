from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from Python_Sql_Requests import get_product_ids_in_cart
from Python_Sql_Requests import (get_client_cart_id, registration_check, get_client_id_by_chat_id, create_order,
                                 add_product_to_order, remove_product_from_cart, get_cart_products)
from Utils import get_chat_id

get_cart_products_router = Router()


@get_cart_products_router.message(F.text == 'Корзина')
async def all_products(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Заказать",
        callback_data="create_order", )
    )
    await message.answer(f"Products: \n{get_cart_products(get_client_cart_id(get_chat_id(message)))}"
                         , reply_markup=builder.as_markup(resize_keyboard=True))


@get_cart_products_router.callback_query(F.data == "create_order")
async def create_order_f(callback: types.CallbackQuery):
    if registration_check(get_client_id_by_chat_id(get_chat_id(callback.message))) is False:
        await callback.message.answer("Клиент не зарегистрирован",
                                       reply_markup=ReplyKeyboardMarkup(
                                           keyboard=[
                                               [
                                                   KeyboardButton(text="Обновить данные клиента")
                                               ]
                                           ]
                                       ))
    else:
        order_id = create_order(get_client_id_by_chat_id(get_chat_id(callback.message)))
        for elem in get_product_ids_in_cart(get_client_cart_id(get_chat_id(callback.message))):
            add_product_to_order(order_id, elem, 1)
            remove_product_from_cart(get_client_cart_id(get_chat_id(callback.message)), elem)
        await callback.message.answer("Заказ оформлен",)
