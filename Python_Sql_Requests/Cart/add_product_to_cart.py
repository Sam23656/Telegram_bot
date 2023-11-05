from Python_Sql_Requests.connect_database import run_connection


def add_product_to_cart(cart_id: int, product_id: int, quantity: int):
    connect, cursor = run_connection()
    cursor.execute("SELECT * FROM add_product_to_cart(%s, %s, %s)", (cart_id, product_id, quantity))
    connect.commit()
    result = 'Продукт добавлен в корзину'
    return result
