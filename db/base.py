import sqlite3
from pathlib import Path


def init_db():
    global db, cur
    DB_NAME = 'db.sqlite'
    MAIN_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(MAIN_PATH/DB_NAME)
    cur = db.cursor()


def create_tables():
    cur.execute(
        """CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            price INTEGER,
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
    db.commit()


def populate_products():
    """
    Заполняем таблицу товаров
    """
    db.execute("""INSERT INTO products (
        name, description, price, photo
    )
    VALUES ('Книга 1', 'Очень интересная книга', 300, './images/cat.webp'),
    ('Книга 2',  'Очень интересная книга', 100, './images/cat.webp'),
    ('Книга 3', 'Очень интересная книга', 200, './images/cat.webp')
    """)
    db.commit()


def get_products():
    """
    Достаем товары из таблицы
    """
    print(cur)
    cur.execute("""
    SELECT * FROM products
    """)
    return cur.fetchall()


def create_order(data):
    """
    Создаем заказ
    """
    cur.execute("""INSERT INTO orders (
        user_name,
        address,
        week_day,
        product_id
    ) VALUES (?, ?, ?, ?)""")
    db.commit()


