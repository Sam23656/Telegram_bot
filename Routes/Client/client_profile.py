from aiogram import types, Router, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from Utils import get_chat_id
from Python_Sql_Requests import get_client_info_by_id
client_profile_router = Router()


@client_profile_router.message(F.text == 'Профиль')
async def all_products(message: types.Message):
    name, surname, is_admin, phone, email, address = get_client_info_by_id(get_chat_id(message))
    await message.answer(f"Имя - {name}\nФамилия - {surname}\n"
                         f"Админ - {is_admin}\nТелефон - {phone}\nEmail - {email}\nАдрес - {address}",
                         reply_markup=ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     KeyboardButton(text="Обновить данные клиента"),
                                     KeyboardButton(text="Назад")
                                 ]
                             ],
                             resize_keyboard=True,
                         ),
                         )
