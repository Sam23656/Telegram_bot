from functools import wraps

from aiogram import Dispatcher, types

from Python_Sql_Requests import get_client_is_admin
from Python_Sql_Requests.Clients.get_client_id_by_chat_id import get_client_id_by_chat_id


def admin_required(func):
    @wraps(func)
    async def wrapper(message: types.Message, *args, **kwargs):
        user_id = message.from_user.id
        if get_client_is_admin(get_client_id_by_chat_id(user_id)) is False:
            await message.answer("У вас нет прав администратора.")
            return

        return await func(message, *args, **kwargs)

    return wrapper
