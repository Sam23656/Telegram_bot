from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile, KeyboardButton, ReplyKeyboardMarkup, Message, ReplyKeyboardRemove

from Python_Sql_Requests import add_product
from Xlsx import convert_xlsx_file_to_df, create_xlsx_file, delete_xlsx_file, get_columns_and_rows
from bot import bot
from Access_Restrictions import admin_required

xlsx_router = Router()


class GetXlsxForm(StatesGroup):
    enter_xlsx = State()


@xlsx_router.message(F.text == 'Получить xlsx файл')
@admin_required
async def upload_xlsx_f(message: types.Message):
    create_xlsx_file()
    await message.answer_document(FSInputFile('./data.xlsx'))
    delete_xlsx_file()


@xlsx_router.message(F.text == 'Отправить xlsx файл')
@admin_required
async def add_xlsx_f(message: types.Message, state: FSMContext):
    await state.set_state(GetXlsxForm.enter_xlsx)
    await message.answer(
        f'Сценарий добавления xlsx файла!\n'
        f'Отправьте xlsx файл',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Назад"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@xlsx_router.message(GetXlsxForm.enter_xlsx)
async def process_product_brand(message: Message, state: FSMContext):
    if message.document:
        file_id = message.document.file_id
        file_info = await bot.get_file(file_id=file_id)
        file = await bot.download_file(file_info.file_path)

        with open('data.xlsx', 'wb') as f:
            f.write(file.read())

        file = convert_xlsx_file_to_df()
        data = get_columns_and_rows(file)
        for elem in data:
            add_product(str(elem[0]), str(elem[1]), int(elem[2]), int(elem[3]), int(elem[4]))
        delete_xlsx_file()
        await message.answer(
            "Файл XLSX успешно загружен и сохранен.",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="Назад"),
                    ]
                ],
                resize_keyboard=True,
            ),
        )
    else:
        await message.answer(
            "Пожалуйста, отправьте файл XLSX.",
            reply_markup=ReplyKeyboardRemove(),
        )

    await state.clear()
