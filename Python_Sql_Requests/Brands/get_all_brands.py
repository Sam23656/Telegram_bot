from Python_Sql_Requests.connect_database import run_connection


def get_all_brands():
    connect, cursor = run_connection()
    cursor.execute("SELECT * FROM GetAllBrands")
    brands = cursor.fetchall()
    result = ""
    for elem in brands:
        for elem2 in elem:
            result += str(elem2)
            result += "   "
        result += "\n"
    if result == '':
        result = "No brands"
    return result
