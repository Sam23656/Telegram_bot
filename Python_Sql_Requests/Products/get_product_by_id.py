from Python_Sql_Requests.connect_database import run_connection


def get_product_by_id(id: int):
    connect, cursor = run_connection()
    cursor.execute(f"SELECT * FROM get_product_by_id('{id}')")
    products = cursor.fetchall()
    result = ""
    i = 1
    for elem in products:
        result += f"{i}. "
        for elem2 in elem:
            result += str(elem2)
            result += "   "
        i += 1
        result += "\n"
    if result == '':
        result = 'Product not found'
    return result
