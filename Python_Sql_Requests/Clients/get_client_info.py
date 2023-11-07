from Python_Sql_Requests.connect_database import run_connection


def get_client_info_by_id(chat_id: str):
    connect, cursor = run_connection()
    cursor.execute(f"SELECT * FROM get_client_info_by_chat_id('{chat_id}')")
    client = cursor.fetchone()
    if not client:
        return 'Client not found'
    is_admin, name, surname, phone, email, address = client
    return name, surname, is_admin, phone, email, address
