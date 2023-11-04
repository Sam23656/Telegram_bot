from Python_Sql_Requests.connect_database import run_connection


def get_all_brands():
    connect, cursor = run_connection()
    cursor.execute("SELECT * FROM GetAllBrands")
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
        result = "No brands"
    return result
