from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from Access_Restrictions import admin_required
from Python_Sql_Requests import get_all_products_id
from Python_Sql_Requests import delete_products_by_id

delete_products_router = Router()


class DeleteProductByIdForm(StatesGroup):
    enter_id = State()


@delete_products_router.message(F.text == 'Удалить по id')
@admin_required
async def delete_product_by_id_f(message: Message, state: FSMContext):
    await state.set_state(DeleteProductByIdForm.enter_id)
    await message.answer(
        f'Сценарий удаления продукта по id! '
        f'Вот список id: \n{get_all_products_id()}'
        f' \nВведи id!',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Отмена"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@delete_products_router.message(DeleteProductByIdForm.enter_id)
async def process_delete_product_f(message: Message, state: FSMContext):
    data = await state.update_data(enter_id=message.text)
    product_id = data['enter_id']
    await state.clear()

    await message.answer(
        f"{delete_products_by_id(product_id)}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Назад")
                ]
            ],
            resize_keyboard=True,
        ),
    )
