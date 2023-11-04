from Python_Sql_Requests.connect_database import run_connection


def delete_products_by_id(id):
    connect, cursor = run_connection()
    cursor.execute(f"SELECT * FROM delete_product_by_id('{id}')")
    connect.commit()
    result = f'Продук по id "{id}" удалён'
    return result
