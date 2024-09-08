import csv
import os


csv_files = [
    "dataset/raw/olist_customers_dataset.csv",
    "dataset/raw/olist_geolocation_dataset.csv",
    "dataset/raw/olist_orders_dataset.csv",
    "dataset/raw/olist_products_dataset.csv",
    "dataset/raw/olist_sellers_dataset.csv",
    "dataset/raw/olist_order_reviews_dataset.csv",
    "dataset/raw/olist_order_payments_dataset.csv",
    "dataset/raw/olist_order_items_dataset.csv" 
]


output_dir = "trimmed_csv_files"
os.makedirs(output_dir, exist_ok=True)

def trim_csv(file_path, output_path, num_lines=5000):
    with open(file_path, "r", newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        
        rows = [header]
        for i, row in enumerate(reader):
            if i >= num_lines:
                break
            rows.append(row)
    
    with open(output_path, "w", newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

for file_path in csv_files:
    output_path = os.path.join(output_dir, os.path.basename(file_path))
    trim_csv(file_path, output_path, num_lines=5000)

print("CSV files have been trimmed and saved successfully.")

