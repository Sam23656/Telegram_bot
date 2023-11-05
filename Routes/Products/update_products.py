from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from Access_Restrictions import admin_required
from Python_Sql_Requests import (get_all_categories, get_all_brands, get_product_by_id, get_category_id_by_name,
                                 get_brand_id_by_name,
                                 update_product)
from Python_Sql_Requests import get_all_products_id

update_products_router = Router()


class UpdateProductForm(StatesGroup):
    enter_id = State()
    enter_str = State()


@update_products_router.message(F.text == 'Обновить продукт')
@admin_required
async def update_product_start(message: Message, state: FSMContext):
    await state.set_state(UpdateProductForm.enter_id)
    await message.answer(
        f'Сценарий обновления продукта!\n'
        f'Вот список id: \n{get_all_products_id()}\n'
        f'Введите id!',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Отмена"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@update_products_router.message(UpdateProductForm.enter_id)
async def update_product_enter_id(message: Message, state: FSMContext):
    data = await state.update_data(enter_id=message.text)
    enter_id = data['enter_id']
    await state.set_state(UpdateProductForm.enter_str)
    await message.answer(
        f'Вот данные продукта: \n{(get_product_by_id(enter_id))}'
        f'Вот список категорий: \n{(get_all_categories())}'
        f'Вот список брендов: \n{(get_all_brands())}'
        f'Введите данные продукта\n'
        f'В формате "Название продукта цена категория бренд описание"',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Отмена"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@update_products_router.message(UpdateProductForm.enter_str)
async def update_product_finish(message: Message, state: FSMContext):
    data = await state.update_data(enter_str=message.text)
    enter_id = data['enter_id']
    enter_str = data['enter_str']
    await state.clear()
    name, price, category, brand, description = enter_str.split(' ')
    category = get_category_id_by_name(category)
    brand = get_brand_id_by_name(brand)
    await message.answer(
        f"{update_product(enter_id, name, description, category, brand, price)}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Назад")
                ]
            ],
            resize_keyboard=True,
        ),
    )
