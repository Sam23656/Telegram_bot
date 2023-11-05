from Python_Sql_Requests.connect_database import run_connection


def get_client_id_by_chat_id(chat_id: int):
    connect, cursor = run_connection()
    cursor.execute(f"SELECT * FROM get_client_id_by_chat_id({chat_id})")
    client_id = cursor.fetchall()[0][0]
    return client_id
