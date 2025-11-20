import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Create Synthetic Data (Simulating a Bank Customer Churn Dataset with skewed churn)
data = {
    'CustomerID': range(1001, 1031),
    'CreditScore': np.concatenate([np.random.randint(400, 850, 25), [np.nan, 700, 650, 550, np.nan]]),
    'Geography': ['France', 'Spain', 'Germany', 'France', 'Spain', 'France', 'Germany', 'Spain', 'France', 'France'] * 3,
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female'] * 3,
    'Tenure': np.concatenate([np.random.randint(0, 10, 28), [np.nan, 5]]), # Tenure in years
    'Balance': np.random.uniform(0, 150000, 30),
    'NumOfProducts': np.random.randint(1, 5, 30),
    'IsActiveMember': np.random.randint(0, 2, 30)
}
df = pd.DataFrame(data)

# Manually create a skewed 'Exited' column (0: Retained, 1: Churned)
# Set up to have higher churn in Germany for a clear pattern.
# France (15): 4 churn
# Spain (9): 2 churn
# Germany (6): 4 churn
exited_list = ([0] * 3 + [1] * 1) * 3 + \
              ([0] * 4 + [1] * 1) * 2 + \
              ([0] * 1 + [1] * 1) * 3 + \
              [0] * 2

# Pad or truncate to ensure length 30
exited_list = exited_list[:30]
df['Exited'] = exited_list
df.loc[15, 'Exited'] = 2 # Introduce inconsistency

# Introduce a small inconsistency in 'Geography' and 'Gender' for cleaning demonstration
df.loc[10, 'Geography'] = 'france' # Inconsistency
df.loc[25, 'Gender'] = 'M' # Inconsistency
df.loc[26, 'Gender'] = 'f' # Inconsistency

# 2. Data Cleaning
# 2.1. Handle Categorical Inconsistencies ('Geography' and 'Gender')
df['Geography'] = df['Geography'].str.title()
df['Gender'] = df['Gender'].replace({'M': 'Male', 'f': 'Female'})

# 2.2. Handle Missing Values (using median for CreditScore and mode for Tenure)
median_credit_score = df['CreditScore'].median()
df['CreditScore'].fillna(median_credit_score, inplace=True)

mode_tenure = df['Tenure'].mode()[0]
df['Tenure'].fillna(mode_tenure, inplace=True)

# Convert Tenure to integer after filling NaN
df['Tenure'] = df['Tenure'].astype(int)

# 2.3. Handle Inconsistencies in 'Exited' (Target Variable)
# Assuming 'Exited' should only be 0 or 1. We will coerce any other value to the mode of the column.
df['Exited'] = df['Exited'].replace(2, df['Exited'].mode()[0]).astype(int)

# Save the cleaned data to CSV for documentation
df.to_csv('cleaned_bank_churn_data.csv', index=False)

# 3. Analysis & Insights

# Insight 1: Churn Rate by Geography
churn_by_geography = df.groupby('Geography')['Exited'].agg(['mean', 'count']).reset_index()
churn_by_geography.rename(columns={'mean': 'ChurnRate', 'count': 'CustomerCount'}, inplace=True)
churn_by_geography['ChurnRate'] = churn_by_geography['ChurnRate'] * 100 # Convert to percentage

# Insight 2: Churn Rate by Tenure Group
# Create tenure groups: 0-2 years (New), 3-5 years (Mid-term), 6+ years (Long-term)
bins = [0, 2, 5, df['Tenure'].max()]
labels = ['0-2 Years (New)', '3-5 Years (Mid-term)', '6+ Years (Long-term)']
df['TenureGroup'] = pd.cut(df['Tenure'], bins=bins, labels=labels, right=True, include_lowest=True)

churn_by_tenure = df.groupby('TenureGroup', observed=True)['Exited'].agg(['mean', 'count']).reset_index()
churn_by_tenure.rename(columns={'mean': 'ChurnRate', 'count': 'CustomerCount'}, inplace=True)
churn_by_tenure['ChurnRate'] = churn_by_tenure['ChurnRate'] * 100 # Convert to percentage

print("\nChurn Rate by Geography (Insight 1):")
print(churn_by_geography)
print("\nChurn Rate by Tenure Group (Insight 2):")
print(churn_by_tenure)

# 4. Visualization

# 4.1. Visualization for Insight 1: Churn Rate by Geography
plt.figure(figsize=(8, 6))
# Sort for better visualization
churn_by_geography_sorted = churn_by_geography.sort_values(by='ChurnRate', ascending=False)
plt.bar(churn_by_geography_sorted['Geography'], churn_by_geography_sorted['ChurnRate'], color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Churn Rate (%) by Customer Geography', fontsize=14)
plt.xlabel('Geography', fontsize=12)
plt.ylabel('Churn Rate (%)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('churn_rate_by_geography.png')
plt.close()

# 4.2. Visualization for Insight 2: Churn Rate by Tenure Group
plt.figure(figsize=(9, 6))
churn_by_tenure_sorted = churn_by_tenure.sort_values(by='ChurnRate', ascending=False)
plt.bar(churn_by_tenure_sorted['TenureGroup'], churn_by_tenure_sorted['ChurnRate'], color=['teal', 'orange', 'purple'])
plt.title('Churn Rate (%) by Customer Tenure Group', fontsize=14)
plt.xlabel('Tenure Group (Years)', fontsize=12)
plt.ylabel('Churn Rate (%)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('churn_rate_by_tenure_group.png')
plt.close()