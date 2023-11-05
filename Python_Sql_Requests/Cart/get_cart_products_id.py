from Python_Sql_Requests.connect_database import run_connection


def get_product_ids_in_cart(client_cart_id: int):
    connect, cursor = run_connection()
    cursor.execute(f"SELECT * FROM get_product_ids_in_cart('{client_cart_id}')")
    products = cursor.fetchall()
    products = [elem[0] for elem in products]
    return products


print(get_product_ids_in_cart(1))