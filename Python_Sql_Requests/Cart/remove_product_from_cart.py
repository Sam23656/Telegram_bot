from Python_Sql_Requests.connect_database import run_connection


def remove_product_from_cart(cart_id: int, product_id: int):
    connect, cursor = run_connection()
    cursor.execute("SELECT * FROM remove_product_from_cart(%s, %s)", (cart_id, product_id))
    connect.commit()
    result = 'Продукт удалён из корзину'
    return result
