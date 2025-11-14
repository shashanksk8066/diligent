import sqlite3
import random
import string

DB_FILE = "ecommerce.db"

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    """Creates the necessary tables in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers (id),
        FOREIGN KEY (product_id) REFERENCES products (id)
    )
    """)

    conn.commit()
    conn.close()


def seed_data():
    """Clears existing data and seeds the database with new sample data."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Clear existing data
    cursor.execute("DELETE FROM orders")
    cursor.execute("DELETE FROM customers")
    cursor.execute("DELETE FROM products")
    # Reset autoincrement counters
    cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('products', 'customers', 'orders');")

    # Sample products
    products = [
        (f'Product {chr(65 + i)}', round(random.uniform(10, 2000), 2)) for i in range(5)
    ]
    cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)

    # Sample customers
    customers = []
    for _ in range(5):
        first_name = ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=5))
        last_name = ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=7))
        name = f"{first_name} {last_name}"
        email = f"{first_name.lower()}.{last_name.lower()}@example.com"
        customers.append((name, email))

    cursor.executemany("INSERT INTO customers (name, email) VALUES (?, ?)", customers)

    # Get product and customer IDs for orders
    product_ids = [row[0] for row in cursor.execute("SELECT id FROM products").fetchall()]
    customer_ids = [row[0] for row in cursor.execute("SELECT id FROM customers").fetchall()]

    # Sample orders
    orders = []
    for _ in range(5):
        customer_id = random.choice(customer_ids)
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 5)
        orders.append((customer_id, product_id, quantity))

    cursor.executemany("INSERT INTO orders (customer_id, product_id, quantity) VALUES (?, ?, ?)", orders)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    seed_data()
    print("Data inserted successfully.")
