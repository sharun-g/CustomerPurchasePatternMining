import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# Aggregate customer data
customer_df = df.groupby('CustomerID').agg({
    'InvoiceNo': 'nunique',
    'TotalAmount': 'sum'
}).reset_index()

customer_df.columns = ['CustomerID', 'Frequency', 'TotalSpend']

# Scale features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(customer_df[['Frequency', 'TotalSpend']])

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
customer_df['Cluster'] = kmeans.fit_predict(scaled_data)

# Save segmentation result
customer_df.to_csv("customer_segments.csv", index=False)

print("✅ Customer Segmentation Completed")
print(customer_df.head())
