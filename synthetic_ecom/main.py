from database import create_tables
from seed import seed_data
from queries import (
    get_all_products,
    get_all_customers,
    get_all_orders,
    get_customer_orders,
    get_order_summary,
)

def main():
    """Main function to run the e-commerce module."""
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
    if customers:
        customer_id_to_check = customers[0].id
        customer_name = customers[0].name
        print(f"\nOrders for Customer #{customer_id_to_check} ({customer_name}):")
        customer_orders = get_customer_orders(customer_id_to_check)
        if customer_orders:
            for order in customer_orders:
                print(f"  - Order #{order['id']}: {order['quantity']} x {order['product_name']} @ ${order['price']:.2f}")
        else:
            print(f"  - No orders found for {customer_name}.")

    # Fetch and print the detailed order summary
    print("\n--- Order Summary ---")
    order_summary = get_order_summary()
    if order_summary:
        for item in order_summary:
            print(
                f"  - Order #{item['order_id']}: "
                f"{item['customer_name']} bought {item['quantity']} x {item['product_name']} "
                f"for a total of ${item['total_price']:.2f}"
            )
    else:
        print("  - No orders to summarize.")


if __name__ == "__main__":
    main()
