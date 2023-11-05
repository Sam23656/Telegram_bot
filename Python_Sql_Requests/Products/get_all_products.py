from Python_Sql_Requests.connect_database import run_connection


def get_all_products():
    connect, cursor = run_connection()
    cursor.execute("SELECT * FROM AllProducts")
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
        result = 'No products'
    return result


def get_all_products_for_xlsx():
    connect, cursor = run_connection()
    cursor.execute("SELECT * FROM get_all_products_for_xlsx()")
    products = cursor.fetchall()
    return products
