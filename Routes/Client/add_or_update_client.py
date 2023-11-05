from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from Python_Sql_Requests import add_or_update_clients
from Utils import get_admin_status, get_chat_id, get_user_name, get_user_surname

add_or_update_client_router = Router()


class AddOrUpdateClientForm(StatesGroup):
    enter_name = State()
    enter_surname = State()
    enter_phone = State()
    enter_email = State()
    enter_address = State()


@add_or_update_client_router.message(Command("start"))
@add_or_update_client_router.message(F.text == 'Обновить данные клиента')
async def add_or_update_client_f(message: Message, state: FSMContext):
    await state.set_state(AddOrUpdateClientForm.enter_name)
    await message.answer(
        f'Сценарий добавления/обновления клиента!\n'
        f'Введите имя клиента\n'
        f'Или нажмите пропустить',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Отмена"),
                    KeyboardButton(text="Пропустить"),
                ]
            ],
            resize_keyboard=True,
        )
    )


@add_or_update_client_router.message(F.text == 'Пропустить')
async def cancel(message: types.Message, state: FSMContext):
    chat_id = get_chat_id(message)
    add_or_update_clients(chat_id, False, get_user_name(message), get_user_surname(message), '', '', '')
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer(f'Пропуск',
                         reply_markup=ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     KeyboardButton(text="Назад")
                                 ]
                             ],
                             resize_keyboard=True, )
                         )


@add_or_update_client_router.message(AddOrUpdateClientForm.enter_name)
async def process_add_or_update_client_f(message: Message, state: FSMContext):
    await state.update_data(enter_name=message.text)
    await state.set_state(AddOrUpdateClientForm.enter_surname)
    await message.answer(
        f'Введите фамилию клиента\n',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@add_or_update_client_router.message(AddOrUpdateClientForm.enter_surname)
async def process_add_or_update_client_f(message: Message, state: FSMContext):
    await state.update_data(enter_surname=message.text)
    await state.set_state(AddOrUpdateClientForm.enter_phone)
    await message.answer(
        f'Введите номер телефона клиента\n',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@add_or_update_client_router.message(AddOrUpdateClientForm.enter_phone)
async def process_add_or_update_client_f(message: Message, state: FSMContext):
    await state.update_data(enter_phone=message.text)
    await state.set_state(AddOrUpdateClientForm.enter_email)
    await message.answer(
        f'Введите email клиента\n',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@add_or_update_client_router.message(AddOrUpdateClientForm.enter_email)
async def process_add_or_update_client_f(message: Message, state: FSMContext):
    await state.update_data(enter_email=message.text)
    await state.set_state(AddOrUpdateClientForm.enter_address)
    await message.answer(
        f'Введите адрес клиента\n',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@add_or_update_client_router.message(AddOrUpdateClientForm.enter_address)
async def process_add_or_update_client_f(message: Message, state: FSMContext):
    date = await state.update_data(enter_address=message.text)
    await state.clear()
    name = date['enter_name']
    surname = date['enter_surname']
    phone = date['enter_phone']
    email = date['enter_email']
    address = date['enter_address']
    is_admin = get_admin_status(name)
    chat_id = get_chat_id(message)
    await message.answer(
        f'{add_or_update_clients(chat_id, is_admin, name, surname, phone, email, address)}',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Назад")
                ]
            ],
            resize_keyboard=True,
        ),
    )
