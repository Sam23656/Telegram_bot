from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from Python_Sql_Requests import get_all_products, get_five_last_products, get_all_categories, \
    get_products_by_category_name

products_router = Router()


class GetProductByCategoryForm(StatesGroup):
    enter_category = State()


@products_router.message(F.text == 'Все продукты')
async def all_products(message: types.Message):
    await message.answer(f"Products: \n{get_all_products()}")


@products_router.message(F.text == 'Последние 5 продуктов')
async def last_five_products(message: types.Message):
    await message.answer(f"Products: \n{get_five_last_products()}")


@products_router.message(F.text == 'Найти по категории')
async def get_product_by_category(message: Message, state: FSMContext):
    await state.set_state(GetProductByCategoryForm.enter_category)
    await message.answer(
        f'Сценарий поиска продукта по категории! '
        f'Вот список категорий: \n{get_all_categories()}'
        f' \nВведи название категории!',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@products_router.message(GetProductByCategoryForm.enter_category)
async def process_product_name(message: Message, state: FSMContext):
    data = await state.update_data(enter_category=message.text)
    category = data['enter_category']
    await state.clear()

    await message.answer(
        f"{get_products_by_category_name(category)}",
    )
