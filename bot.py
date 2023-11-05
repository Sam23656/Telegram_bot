import asyncio
import logging
import os

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F

from Routes import *

load_dotenv()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.environ.get("BOT_TOKEN_CODE"))
dp = Dispatcher()


@dp.message(F.text == 'Назад')
@dp.message(Command("Buttons"))
async def cmd_special_buttons(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Все продукты"),
        types.KeyboardButton(text="Последние 10 продуктов"),
        types.KeyboardButton(text="Найти по id"),
        types.KeyboardButton(text="Найти по бренду"),
        types.KeyboardButton(text="Найти по категории"),
        types.KeyboardButton(text="Добавить продукт"),
        types.KeyboardButton(text="Обновить продукт"),
        types.KeyboardButton(text="Удалить продукт"),
        types.KeyboardButton(text="Профиль"),
    )
    await message.answer(
        "Выберите действие:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )


@dp.message(F.text == 'Отмена')
async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer('Отменено', reply_markup=types.ReplyKeyboardRemove())


async def main():
    routes = [get_products_router, categories_router, brands_router, delete_products_router, add_products_router,
              update_products_router, add_or_update_client_router, client_profile_router]
    for route in routes:
        dp.include_router(route)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
