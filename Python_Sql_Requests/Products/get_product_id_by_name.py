from Python_Sql_Requests.connect_database import run_connection


def get_product_id_by_name(product_name: str):
    connect, cursor = run_connection()
    cursor.execute(f"SELECT * FROM get_product_id_by_name('{product_name}')")
    result = cursor.fetchall()[0][0]
    return result
