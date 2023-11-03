from Python_Sql_Requests.connect_database import run_connection


def get_all_products():
    connect, cursor = run_connection()
    cursor.execute("SELECT * FROM ProductsWithCategories")
    products = cursor.fetchall()
    result = ""
    for elem in products:
        for elem2 in elem:
            result += str(elem2)
            result += "   "
        result += "\n"
    return result
