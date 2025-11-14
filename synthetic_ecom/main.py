import os
from database import create_tables
from seed import seed_data
from queries import (
    get_all_products,
    get_all_customers,
    get_all_orders,
    get_customer_orders,
)

DB_FILE = "ecommerce.db"

def main():
    """Main function to run the e-commerce module."""
    # Start with a clean database file
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"Removed existing database file: {DB_FILE}")

    # Create database and tables
    create_tables()
    print("Database tables created.")

    # Seed the database with sample data
    seed_data()
    print("Database seeded.")

    print("\n--- Sample Data ---")

    # Fetch and print all products
    print("\nProducts:")
    products = get_all_products()
    for product in products:
        print(f"  - {product.name}: ${product.price:.2f}")

    # Fetch and print all customers
    print("\nCustomers:")
    customers = get_all_customers()
    for customer in customers:
        print(f"  - {customer.name} ({customer.email})")

    # Fetch and print all orders
    print("\nOrders:")
    orders = get_all_orders()
    for order in orders:
        print(f"  - Order #{order.id}: Customer #{order.customer_id}, Product #{order.product_id}, Quantity: {order.quantity}")

    # Fetch and print orders for a specific customer
    print("\nOrders for Customer #1 (Alice Smith):")
    customer_orders = get_customer_orders(1)
    for order in customer_orders:
        print(f"  - Order #{order['id']}: {order['quantity']} x {order['product_name']} @ ${order['price']:.2f}")


if __name__ == "__main__":
    main()
