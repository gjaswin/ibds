import csv
from datetime import datetime

def extract(file_path):
    """Extracts data from a CSV file."""
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def transform(data):
    """Transforms the data by cleaning and formatting."""
    transformed_data = []
    for row in data:
        # Rule 1: Remove rows with null OrderID
        if row.get('OrderID') and row['OrderID'].strip():
            # Rule 2: Format date to YYYY-MM-DD
            for date_format in ['%Y-%m-%d', '%Y/%m/%d', '%Y.%m.%d']:
                try:
                    row['Date'] = datetime.strptime(row['Date'], date_format).strftime('%Y-%m-%d')
                    break
                except (ValueError, TypeError):
                    continue
            transformed_data.append(row)
    return transformed_data

def load(file_path, data):
    """Loads the data into a new CSV file."""
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def main():
    """Main function to run the ETL pipeline."""
    # Extract
    print("Step 1: Extracting data from sales_data.csv...")
    sales_data = extract('sales_data.csv')
    print("Extraction complete.")
    print("-" * 20)

    # Transform
    print("Step 2: Transforming data...")
    print("Applying transformation rules:")
    print("  - Removing rows with null OrderID.")
    print("  - Formatting dates to YYYY-MM-DD.")
    cleaned_data = transform(sales_data)
    print("Transformation complete.")
    print("-" * 20)

    # Load
    print("Step 3: Loading data into cleaned_sales_data.csv...")
    load('cleaned_sales_data.csv', cleaned_data)
    print("Loading complete.")
    print("-" * 20)

    # Display loaded data
    print("Loaded Data:")
    with open('cleaned_sales_data.csv', 'r') as file:
        print(file.read())

if __name__ == "__main__":
    main()
