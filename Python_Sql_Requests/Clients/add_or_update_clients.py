from Python_Sql_Requests.connect_database import run_connection


def add_or_update_clients(chat_id: int, is_admin: bool, name: str, surname: str, phone: str or None, email: str or None,
                          address:  str or None):
    connect, cursor = run_connection()
    cursor.execute("SELECT * FROM add_or_update_client(%s, %s, %s, %s, %s, %s, %s)", (chat_id, is_admin, name,
                                                                                      surname, phone, email, address))
    connect.commit()
    result = 'Клиент добавлен или обновлен'
    return result
