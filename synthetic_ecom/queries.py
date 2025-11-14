from database import get_db_connection
from models import Product, Customer, Order

def get_all_products():
    """Retrieves all products from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = [Product(**row) for row in cursor.fetchall()]
    conn.close()
    return products

def get_all_customers():
    """Retrieves all customers from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = [Customer(**row) for row in cursor.fetchall()]
    conn.close()
    return customers

def get_all_orders():
    """Retrieves all orders from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = [Order(**row) for row in cursor.fetchall()]
    conn.close()
    return orders

def get_customer_orders(customer_id: int):
    """Retrieves all orders for a specific customer."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT o.id, o.quantity, p.name as product_name, p.price
        FROM orders o
        JOIN products p ON o.product_id = p.id
        WHERE o.customer_id = ?
    """, (customer_id,))
    orders = cursor.fetchall()
    conn.close()
    return orders

def get_order_summary():
    """
    Retrieves a summary of all orders, joining products and customers.
    Returns a list of dictionaries.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            o.id AS order_id,
            c.name AS customer_name,
            p.name AS product_name,
            o.quantity,
            (o.quantity * p.price) AS total_price
        FROM orders o
        JOIN customers c ON o.customer_id = c.id
        JOIN products p ON o.product_id = p.id
    """)
    # Convert rows to a list of dictionaries
    summary = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return summary
