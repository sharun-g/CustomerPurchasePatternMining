import pandas as pd

# Load dataset (BOM-safe)
df = pd.read_csv("dataset/OnlineRetail.csv", encoding="utf-8-sig")

# Clean column names
df.columns = df.columns.str.strip()
print("Columns after fix:", df.columns)

# Remove missing values
df.dropna(inplace=True)

# Remove cancelled invoices
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# Convert date (DD-MM-YYYY format)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True)

# Calculate total amount
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("---Preprocessing completed successfully!---")
print(df.head())
