from Python_Sql_Requests.connect_database import run_connection


def get_brand_id_by_name(name: str):
    connect, cursor = run_connection()
    cursor.execute(f"SELECT * FROM get_brand_id_by_name('{name}')")
    result = int(cursor.fetchall()[0][0])
    return result
