from Python_Sql_Requests.connect_database import run_connection


def get_all_categories():
    connect, cursor = run_connection()
    cursor.execute("SELECT * FROM GetAllCategories")
    categories = cursor.fetchall()
    result = ""
    for elem in categories:
        for elem2 in elem:
            result += str(elem2)
            result += "   "
        result += "\n"
    if result == '':
        result = 'No categories'
    return result
