import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# Create transaction list using InvoiceNo and Description
transactions = (
    df.groupby('InvoiceNo')['Description']
    .apply(list)
    .tolist()
)

# Encode transactions
te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
encoded_df = pd.DataFrame(te_array, columns=te.columns_)

# Apply Apriori
frequent_itemsets = apriori(encoded_df, min_support=0.005, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)

# Save rules
rules.to_csv("association_rules.csv", index=False)

print("✅ Market Basket Analysis Completed")
print(rules[['antecedents', 'consequents', 'support', 'confidence']].head())
