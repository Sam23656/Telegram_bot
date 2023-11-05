from Python_Sql_Requests.connect_database import run_connection


def create_order(client_id: int):
    connect, cursor = run_connection()
    cursor.execute(f"SELECT * FROM create_order({client_id})")
    connect.commit()
    result = cursor.fetchone()
    return result
