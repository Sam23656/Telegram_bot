from Python_Sql_Requests.connect_database import run_connection


def add_or_update_clients(chat_id: str, is_admin: bool, name: str, surname: str or "", phone: str or "", email: str or "",
                          address:  str or ""):
    connect, cursor = run_connection()
    chat_id = str(chat_id)
    cursor.execute("SELECT * FROM add_or_update_client(%s, %s, %s, %s, %s, %s, %s)", (chat_id, is_admin, name,
                                                                                      surname, phone, email, address))
    connect.commit()
    result = 'Клиент добавлен или обновлен'
    return result

