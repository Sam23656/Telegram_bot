from aiogram import types, Router, F
from aiogram.types import FSInputFile

from Access_Restrictions import admin_required
from Xlsx import create_xlsx_file, delete_xlsx_file

get_xlsx_router = Router()


@get_xlsx_router.message(F.text == 'Получить xlsx файл')
@admin_required
async def upload_xlsx_f(message: types.Message):
    create_xlsx_file()
    await message.answer_document(FSInputFile('./data.xlsx'))
    delete_xlsx_file()

