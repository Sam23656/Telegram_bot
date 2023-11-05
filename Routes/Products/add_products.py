from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from Python_Sql_Requests import get_all_categories, get_all_brands, get_category_id_by_name, get_brand_id_by_name, add_product

add_products_router = Router()


class AddProductByForm(StatesGroup):
    enter_str = State()


@add_products_router.message(F.text == 'Добавить продукт')
async def add_product_f(message: Message, state: FSMContext):
    await state.set_state(AddProductByForm.enter_str)
    await message.answer(
        f'Сценарий добавления продукта!\n'
        f'Вот список категорий: \n{(get_all_categories())}'
        f'Вот список брендов: \n{(get_all_brands())}'
        f'Введите данные продукта\n'
        f'В формате "Название продукта цена категория бренд описание"',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@add_products_router.message(AddProductByForm.enter_str)
async def process_add_product_f(message: Message, state: FSMContext):
    data = await state.update_data(enter_str=message.text)
    enter_str = data['enter_str']
    await state.clear()
    name, price, category, brand, description = enter_str.split(' ')
    category = get_category_id_by_name(category)
    brand = get_brand_id_by_name(brand)
    await message.answer(
        f"{add_product(name, description, category, brand, price)}",
    )
