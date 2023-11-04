from .connect_database import run_connection


def get_ten_last_products():
    connect, cursor = run_connection()
    cursor.execute("SELECT * FROM Last10Products")
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
    return result
