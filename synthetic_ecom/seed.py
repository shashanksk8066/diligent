from database import get_db_connection

def seed_data():
    """Seeds the database with sample data."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Sample products
    products = [
        ('Laptop', 999.99),
        ('Mouse', 25.50),
        ('Keyboard', 75.00),
        ('Monitor', 300.00),
        ('Webcam', 50.00)
    ]
    cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)

    # Sample customers
    customers = [
        ('Alice Smith', 'alice@example.com'),
        ('Bob Johnson', 'bob@example.com'),
        ('Charlie Brown', 'charlie@example.com'),
        ('Diana Prince', 'diana@example.com'),
        ('Ethan Hunt', 'ethan@example.com')
    ]
    cursor.executemany("INSERT INTO customers (name, email) VALUES (?, ?)", customers)

    # Sample orders
    orders = [
        (1, 1, 1),
        (2, 2, 2),
        (3, 3, 1),
        (4, 4, 3),
        (5, 5, 1)
    ]
    cursor.executemany("INSERT INTO orders (customer_id, product_id, quantity) VALUES (?, ?, ?)", orders)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    seed_data()
    print("Database seeded with sample data.")
