from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from Python_Sql_Requests import (get_all_products, get_all_products_id, get_product_by_id, get_all_categories,
                                 get_products_by_brand_name, get_products_by_category_name, get_ten_last_products,
                                 get_all_brands)

get_products_router = Router()


class GetProductByCategoryForm(StatesGroup):
    enter_category = State()


class GetProductByBrandForm(StatesGroup):
    enter_brand = State()


class GetProductByIdForm(StatesGroup):
    enter_id = State()


@get_products_router.message(F.text == 'Все продукты')
async def all_products(message: types.Message):
    await message.answer(f"Products: \n{get_all_products()}")


@get_products_router.message(F.text == 'Последние 10 продуктов')
async def last_ten_products(message: types.Message):
    await message.answer(f"Products: \n{get_ten_last_products()}")


@get_products_router.message(F.text == 'Найти по категории')
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


@get_products_router.message(GetProductByCategoryForm.enter_category)
async def process_product_category(message: Message, state: FSMContext):
    data = await state.update_data(enter_category=message.text)
    category = data['enter_category']
    await state.clear()

    await message.answer(
        f"{get_products_by_category_name(category)}",
    )


@get_products_router.message(F.text == 'Найти по бренду')
async def get_product_by_brand(message: Message, state: FSMContext):
    await state.set_state(GetProductByBrandForm.enter_brand)
    await message.answer(
        f'Сценарий поиска продукта по бренду! '
        f'Вот список брендов: \n{get_all_brands()}'
        f' \nВведи название бренда!',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@get_products_router.message(GetProductByBrandForm.enter_brand)
async def process_product_brand(message: Message, state: FSMContext):
    data = await state.update_data(enter_brand=message.text)
    brand = data['enter_brand']
    await state.clear()

    await message.answer(
        f"{get_products_by_brand_name(brand)}",
    )


@get_products_router.message(F.text == 'Найти по id')
async def state_get_product_by_id(message: Message, state: FSMContext):
    await state.set_state(GetProductByIdForm.enter_id)
    await message.answer(
        f'Сценарий поиска продукта по id! '
        f'Вот список id: \n{get_all_products_id()}'
        f' \nВведи id!',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@get_products_router.message(GetProductByIdForm.enter_id)
async def process_product_id(message: Message, state: FSMContext):
    data = await state.update_data(enter_id=message.text)
    id = data['enter_id']
    await state.clear()

    await message.answer(
        f"{get_product_by_id(id)}",
    )
