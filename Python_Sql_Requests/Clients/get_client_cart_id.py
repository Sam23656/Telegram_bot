from Python_Sql_Requests.connect_database import run_connection


def get_client_cart_id(chat_id: str):
    connect, cursor = run_connection()
    cursor.execute(f"SELECT * FROM get_client_cart_id('{chat_id}')")
    result = cursor.fetchall()[0][0]
    return result
