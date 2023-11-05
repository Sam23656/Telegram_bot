from Python_Sql_Requests.connect_database import run_connection


def update_product(product_id: int, name: str, description: str, category_id: int, brand_id: int, price: int):
    connect, cursor = run_connection()
    cursor.execute("SELECT * FROM update_product(%s, %s, %s, %s, %s, %s)",
                   (product_id, name, description, category_id, brand_id, price))
    connect.commit()
    result = 'Продукт обновлен'
    return result
