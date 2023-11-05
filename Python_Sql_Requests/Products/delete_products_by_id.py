from Python_Sql_Requests.connect_database import run_connection


def delete_products_by_id(product_id: int):
    connect, cursor = run_connection()
    cursor.execute(f"SELECT * FROM delete_product_by_id('{product_id}')")
    connect.commit()
    result = f'Продукт по id "{product_id}" удалён'
    return result
