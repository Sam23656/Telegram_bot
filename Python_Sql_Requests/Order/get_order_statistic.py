from Python_Sql_Requests.connect_database import run_connection


def get_order_statistic(chat_id: int):
    connect, cursor = run_connection()
    cursor.execute(f"SELECT * FROM get_order_statistics({chat_id})")
    result = cursor.fetchall()

    order_id = None
    order_date = None
    products = []
    result2 = ''

    for elem in result:
        if elem[0] != order_id:
            if order_id is not None:
                result2 += f"Order ID: {order_id}\n"
                result2 += f"Order Date: {order_date}\n"
                for product in products:
                    result2 += f"Product: {product[0]}, Quantity: {product[1]}\n"
                result2 += "\n"

            order_id = elem[0]
            order_date = elem[1]
            products = [(elem[2], elem[3])]
        else:
            products.append((elem[2], elem[3]))

    if order_id is not None:
        result2 += f"Order ID: {order_id}\n"
        result2 += f"Order Date: {order_date}\n"
        for product in products:
            result2 += f"Product: {product[0]}, Quantity: {product[1]}\n"

    return result2

