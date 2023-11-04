from aiogram.exceptions import TelegramBadRequest

from Python_Sql_Requests.connect_database import run_connection


def get_products_by_brand_name(brand_name):
    connect, cursor = run_connection()
    cursor.execute(f"SELECT * FROM get_products_by_brand('{brand_name}')")
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
    if result == "":
        result = "No products"
    return result
