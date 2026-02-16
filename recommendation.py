#-static product recommendation
'''
import pandas as pd

rules = pd.read_csv("association_rules.csv")

rules['antecedents'] = rules['antecedents'].astype(str)
rules['consequents'] = rules['consequents'].astype(str)

def recommend_products(product_name):
    recs = rules[
        (rules['antecedents'].str.contains(product_name, case=False)) |
        (rules['consequents'].str.contains(product_name, case=False))
    ][['antecedents', 'consequents', 'confidence']]

    return recs.sort_values(by='confidence', ascending=False).head(5)

product = "WHITE HANGING HEART T-LIGHT HOLDER"
print("Recommendations for:", product)
print(recommend_products(product))

'''
#-dynamic product recomendation
import pandas as pd

# Load association rules
rules = pd.read_csv("association_rules.csv")

# Convert columns to string (important)
rules['antecedents'] = rules['antecedents'].astype(str)
rules['consequents'] = rules['consequents'].astype(str)

def recommend_products(product_name):
    recs = rules[
        (rules['antecedents'].str.contains(product_name, case=False)) |
        (rules['consequents'].str.contains(product_name, case=False))
    ][['antecedents', 'consequents', 'confidence']]

    return recs.sort_values(by='confidence', ascending=False).head(5)

# USER INPUT
while True:
    product = input("\nEnter product name (or type 'exit' to quit): ")

    if product.lower() == "exit":
        print("Exiting recommendation system.")
        break

    recommendations = recommend_products(product)

    if recommendations.empty:
        print(" No strong recommendations found for this product.")
    else:
        print("\n Recommended Products:")
        print(recommendations)
