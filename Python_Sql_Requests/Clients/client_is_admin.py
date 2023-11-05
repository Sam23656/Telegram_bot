from Python_Sql_Requests.connect_database import run_connection


def get_client_is_admin(user_id: int):
    connect, cursor = run_connection()
    cursor.execute(f"SELECT * FROM get_user_is_admin({user_id})")
    result = cursor.fetchone()[0]
    return result