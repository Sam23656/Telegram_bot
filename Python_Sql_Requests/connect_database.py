import psycopg2
import os
from dotenv import load_dotenv


def run_connection():
    load_dotenv()
    connection = psycopg2.connect(
        f"host=127.0.0.1 dbname=product_shop user={os.environ.get('PGUSERNAME')} password={os.environ.get('PASSWORD')}")
    cursor = connection.cursor()
    return connection, cursor
