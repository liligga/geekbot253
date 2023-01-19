import datetime
import sqlite3
from pathlib import Path


DB_NAME = 'db.sqlite'
MAIN_PATH = Path(__file__).parent.parent
connection = sqlite3.connect(MAIN_PATH/DB_NAME)
cur = connection.cursor()


def create_tables(cur):
    """
    для создания таблиц 'Товары' 
    и 'Заказы' в БД.
    """
    cur.execute(
        """CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            photo TEXT
        )"""
    )
    cur.execute(
        """CREATE TABLE IF NOT EXISTS orders(
            order_id INTEGER PRIMARY KEY,
            user_name TEXT,
            address TEXT,
            week_day TEXT,
            product_id INTEGER,
            FOREIGN KEY (product_id) 
                REFERENCES products (product_id) 
                ON DELETE CASCADE 
        )
        """
    )
    


def populate_products(cur):
    """
    Заполняем таблицу товаров
    """
    cur.execute("""INSERT INTO products (
        name, description, photo
    )
    VALUES(1, 'Книга 1',
    'Очень интересная книга',
    './images/cat.webp')
    """)




def get_products(cur):
    """
    Достаем товары из таблицы, по страницам
    """
    cur.execute("""
    SELECT * FROM products
    """)
    return cur.fetchall()


def create_order(cur):
    """
    Создаем заказ
    """
    cur.execute("""INSERT INTO orders (
        user_name,
        address,
        week_day,
        product_id
    ) VALUES (?, ?, ?, ?)""")

create_tables(cur)
# populate_products(cur)

connection.commit()
connection.close()