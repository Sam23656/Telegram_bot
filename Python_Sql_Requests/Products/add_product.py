from Python_Sql_Requests.connect_database import run_connection


def add_product(name: str, description: str, category_id: int, brand_id: int, price: int):
    connect, cursor = run_connection()
    cursor.execute("SELECT * FROM add_product(%s, %s, %s, %s, %s)", (name, description, category_id, brand_id, price))
    connect.commit()
    result = 'Продукт добавлен'
    return result
