import pandas as pd
import os

# File paths
customer_file = "dataset/trimmed_csv_files/olist_customers_dataset.csv"
geolocation_file = "dataset/trimmed_csv_files/olist_geolocation_dataset.csv"
order_items_file = "dataset/trimmed_csv_files/olist_order_items_dataset.csv"
order_payments_file = "dataset/trimmed_csv_files/olist_order_payments_dataset.csv"
order_reviews_file = "dataset/trimmed_csv_files/olist_order_reviews_dataset.csv"
orders_file = "dataset/trimmed_csv_files/olist_orders_dataset.csv"
products_file = "dataset/trimmed_csv_files/olist_products_dataset.csv"
sellers_file = "dataset/trimmed_csv_files/olist_sellers_dataset.csv"

# Output directory
output_dir = "cypher_queries"
os.makedirs(output_dir, exist_ok=True)

# Read CSV files
customers = pd.read_csv(customer_file)
geolocations = pd.read_csv(geolocation_file)
order_items = pd.read_csv(order_items_file)
order_payments = pd.read_csv(order_payments_file)
order_reviews = pd.read_csv(order_reviews_file)
orders = pd.read_csv(orders_file)
products = pd.read_csv(products_file)
sellers = pd.read_csv(sellers_file)

# Function to escape values
def escape_value(value):
    if pd.isna(value):
        return "NULL"
    value = str(value).replace('"', '\\"').replace("\n", "\\n")
    return f'"{value}"' if not value.isnumeric() else value

# Functions to generate queries
def generate_customer_queries(df):
    queries = []
    for _, row in df.iterrows():
        query = (
            f"CREATE (c:Customer {{ "
            f'customer_id: {escape_value(row["customer_id"])}, '
            f'customer_unique_id: {escape_value(row["customer_unique_id"])}, '
            f'customer_zip_code_prefix: {escape_value(row["customer_zip_code_prefix"])}, '
            f'customer_city: {escape_value(row["customer_city"])}, '
            f'customer_state: {escape_value(row["customer_state"])} }});'
        )
        queries.append(query)
    return queries

def generate_geolocation_queries(df):
    queries = []
    for _, row in df.iterrows():
        query = (
            f"CREATE (g:Geolocation {{ "
            f'geolocation_zip_code_prefix: {escape_value(row["geolocation_zip_code_prefix"])}, '
            f'geolocation_lat: {row["geolocation_lat"]}, '
            f'geolocation_lng: {row["geolocation_lng"]}, '
            f'geolocation_city: {escape_value(row["geolocation_city"])}, '
            f'geolocation_state: {escape_value(row["geolocation_state"])} }});'
        )
        queries.append(query)
    return queries

def generate_order_items_queries(df):
    queries = []
    for _, row in df.iterrows():
        query = (
            f"CREATE (oi:OrderItem {{ "
            f'order_id: {escape_value(row["order_id"])}, '
            f'order_item_id: {row["order_item_id"]}, '
            f'product_id: {escape_value(row["product_id"])}, '
            f'seller_id: {escape_value(row["seller_id"])}, '
            f'shipping_limit_date: {escape_value(row["shipping_limit_date"])}, '
            f'price: {row["price"]}, '
            f'freight_value: {row["freight_value"]} }});'
        )
        queries.append(query)
    return queries

def generate_order_payments_queries(df):
    queries = []
    for _, row in df.iterrows():
        query = (
            f"CREATE (op:OrderPayment {{ "
            f'order_id: {escape_value(row["order_id"])}, '
            f'payment_sequential: {row["payment_sequential"]}, '
            f'payment_type: {escape_value(row["payment_type"])}, '
            f'payment_installments: {row["payment_installments"]}, '
            f'payment_value: {row["payment_value"]} }});'
        )
        queries.append(query)
    return queries

def generate_order_reviews_queries(df):
    queries = []
    for _, row in df.iterrows():
        query = (
            f"CREATE (or:OrderReview {{ "
            f'review_id: {escape_value(row["review_id"])}, '
            f'order_id: {escape_value(row["order_id"])}, '
            f'review_score: {row["review_score"]}, '
            f'review_comment_title: {escape_value(row["review_comment_title"])}, '
            f'review_comment_message: {escape_value(row["review_comment_message"])}, '
            f'review_creation_date: {escape_value(row["review_creation_date"])}, '
            f'review_answer_timestamp: {escape_value(row["review_answer_timestamp"])} }});'
        )
        queries.append(query)
    return queries

def generate_orders_queries(df):
    queries = []
    for _, row in df.iterrows():
        query = (
            f"CREATE (o:Order {{ "
            f'order_id: {escape_value(row["order_id"])}, '
            f'customer_id: {escape_value(row["customer_id"])}, '
            f'order_status: {escape_value(row["order_status"])}, '
            f'order_purchase_timestamp: {escape_value(row["order_purchase_timestamp"])}, '
            f'order_approved_at: {escape_value(row["order_approved_at"])}, '
            f'order_delivered_carrier_date: {escape_value(row["order_delivered_carrier_date"])}, '
            f'order_delivered_customer_date: {escape_value(row["order_delivered_customer_date"])}, '
            f'order_estimated_delivery_date: {escape_value(row["order_estimated_delivery_date"])} }});'
        )
        queries.append(query)
    return queries

def generate_products_queries(df):
    queries = []
    for _, row in df.iterrows():
        query = (
            f"CREATE (p:Product {{ "
            f'product_id: {escape_value(row["product_id"])}, '
            f'product_category_name: {escape_value(row["product_category_name"])}, '
            f'product_name_length: {row["product_name_length"]}, '
            f'product_description_length: {row["product_description_length"]}, '
            f'product_photos_qty: {row["product_photos_qty"]}, '
            f'product_weight_g: {row["product_weight_g"]}, '
            f'product_length_cm: {row["product_length_cm"]}, '
            f'product_height_cm: {row["product_height_cm"]}, '
            f'product_width_cm: {row["product_width_cm"]} }});'
        )
        queries.append(query)
    return queries

def generate_sellers_queries(df):
    queries = []
    for _, row in df.iterrows():
        query = (
            f"CREATE (s:Seller {{ "
            f'seller_id: {escape_value(row["seller_id"])}, '
            f'seller_zip_code_prefix: {escape_value(row["seller_zip_code_prefix"])}, '
            f'seller_city: {escape_value(row["seller_city"])}, '
            f'seller_state: {escape_value(row["seller_state"])} }});'
        )
        queries.append(query)
    return queries

def generate_relationship_queries(
    customers, orders, order_items, order_payments, order_reviews, products, sellers
):
    queries = []

    for _, row in orders.iterrows():
        queries.append(
            f"MATCH (c:Customer), (o:Order) "
            f"WHERE c.customer_id = {escape_value(row['customer_id'])} AND o.order_id = {escape_value(row['order_id'])} "
            f"CREATE (c)-[:PLACED]->(o);"
        )

    for _, row in order_items.iterrows():
        queries.append(
            f"MATCH (o:Order), (oi:OrderItem) "
            f"WHERE o.order_id = {escape_value(row['order_id'])} AND oi.order_id = {escape_value(row['order_id'])} "
            f"CREATE (o)-[:CONTAINS]->(oi);"
        )

    for _, row in order_items.iterrows():
        queries.append(
            f"MATCH (oi:OrderItem), (p:Product) "
            f"WHERE oi.product_id = {escape_value(row['product_id'])} AND p.product_id = {escape_value(row['product_id'])} "
            f"CREATE (oi)-[:INCLUDES]->(p);"
        )

    for _, row in order_items.iterrows():
        queries.append(
            f"MATCH (oi:OrderItem), (s:Seller) "
            f"WHERE oi.seller_id = {escape_value(row['seller_id'])} AND s.seller_id = {escape_value(row['seller_id'])} "
            f"CREATE (oi)-[:SOLD_BY]->(s);"
        )

    for _, row in order_payments.iterrows():
        queries.append(
            f"MATCH (o:Order), (op:OrderPayment) "
            f"WHERE o.order_id = {escape_value(row['order_id'])} AND op.order_id = {escape_value(row['order_id'])} "
            f"CREATE (o)-[:HAS_PAYMENT]->(op);"
        )

    for _, row in order_reviews.iterrows():
        queries.append(
            f"MATCH (o:Order), (or:OrderReview) "
            f"WHERE o.order_id = {escape_value(row['order_id'])} AND or.order_id = {escape_value(row['order_id'])} "
            f"CREATE (o)-[:HAS_REVIEW]->(or);"
        )

    return queries

# Function to write queries to files with line limit
def write_queries_to_file(queries, file_name, output_dir, lines_per_file=50):
    os.makedirs(output_dir, exist_ok=True)
    file_index = 1
    for i in range(0, len(queries), lines_per_file):
        chunk = queries[i:i + lines_per_file]
        chunk_file_name = f"{file_name}_{file_index}.cypher" if file_index > 1 else f"{file_name}.cypher"
        with open(os.path.join(output_dir, chunk_file_name), 'w') as file:
            file.write("\n".join(chunk))
        file_index += 1

# Generate queries
customer_queries = generate_customer_queries(customers)
geolocation_queries = generate_geolocation_queries(geolocations)
order_items_queries = generate_order_items_queries(order_items)
order_payments_queries = generate_order_payments_queries(order_payments)
order_reviews_queries = generate_order_reviews_queries(order_reviews)
orders_queries = generate_orders_queries(orders)
products_queries = generate_products_queries(products)
sellers_queries = generate_sellers_queries(sellers)
relationship_queries = generate_relationship_queries(customers, orders, order_items, order_payments, order_reviews, products, sellers)

# Write queries to files with line limit
write_queries_to_file(customer_queries, "customer_queries", output_dir)
write_queries_to_file(geolocation_queries, "geolocation_queries", output_dir)
write_queries_to_file(order_items_queries, "order_items_queries", output_dir)
write_queries_to_file(order_payments_queries, "order_payments_queries", output_dir)
write_queries_to_file(order_reviews_queries, "order_reviews_queries", output_dir)
write_queries_to_file(orders_queries, "orders_queries", output_dir)
write_queries_to_file(products_queries, "products_queries", output_dir)
write_queries_to_file(sellers_queries, "sellers_queries", output_dir)
write_queries_to_file(relationship_queries, "relationship_queries", output_dir)

