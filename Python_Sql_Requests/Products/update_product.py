from Python_Sql_Requests.connect_database import run_connection


def update_product(id, name, description, category_id, brand_id, price):
    connect, cursor = run_connection()
    cursor.execute("SELECT * FROM update_product(%s, %s, %s, %s, %s, %s)",
                   (id, name, description, category_id, brand_id, price))
    connect.commit()
    result = 'Продукт обновлен'
    return result
