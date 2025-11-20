
import csv
import random

def generate_churn_dataset(filename="customer_churn.csv", num_rows=1000):
    fieldnames = ["CustomerID", "Age", "Gender", "Tenure", "MonthlyCharges", "Churn"]
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1, num_rows + 1):
            churn = random.choice([0, 1])
            writer.writerow({
                "CustomerID": i,
                "Age": random.randint(18, 70),
                "Gender": random.choice(["Male", "Female"]),
                "Tenure": random.randint(0, 60),
                "MonthlyCharges": round(random.uniform(20, 120), 2),
                "Churn": churn
            })

if __name__ == "__main__":
    generate_churn_dataset()
    print("Customer churn dataset generated successfully.")
