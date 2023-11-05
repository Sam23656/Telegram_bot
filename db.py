TOKEN = input("Введите токен: ")
with open('.env', 'w') as env_file:
    env_file.write(f'BOT_TOKEN_CODE={TOKEN}')

PGUSERNAME = input("Введите имя пользователя postgres: ")
PASSWORD = input("Введите пароль: ")
with open('Python_Sql_Requests/.env', 'w') as env_file:
    env_file.write(f'PGUSERNAME={PGUSERNAME}\n')
    env_file.write(f'PASSWORD={PASSWORD}')

db_params = {
    "dbname": "product_shop",
    "user": f"{PGUSERNAME}",
    "password": f"{PASSWORD}",
    "host": "127.0.0.1",
    "port": "5432"
}

sql_file_path = ["./Sql/create.sql", "./Sql/insert.sql", "./Sql/view.sql", "./Sql/function.sql", "./Sql/function2.sql",
                 "./Sql/function3.sql"]

import psycopg2
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

for sql_file in sql_file_path:
    with open(sql_file, "r") as sql_file:
        sql_query = sql_file.read()
        cur.execute(sql_query)
        conn.commit()
        sql_file.close()

cur.close()
conn.close()
