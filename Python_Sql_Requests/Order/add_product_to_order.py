from Python_Sql_Requests.connect_database import run_connection


def add_product_to_order(order_id: int, product_id: int, quantity: int):
    connect, cursor = run_connection()
    cursor.execute("SELECT * FROM add_product_to_order(%s, %s, %s)", (order_id, product_id, quantity))
    connect.commit()
    result = cursor.fetchone()
    return result
