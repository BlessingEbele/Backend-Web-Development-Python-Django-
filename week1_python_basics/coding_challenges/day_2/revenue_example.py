products = ["rice", "beans", "yam", "rice", "beans", "oil", "yam"]
quantities = [10, 5, 8, 6, 7, 3, 2]
prices = [500, 300, 200, 500, 300, 1000, 200] 

# 1️⃣ List & Integer Operations

# Calculate **total items sold**
TotalItemSold = sum(quantities)
print(f"Total items sold: {TotalItemSold}")

# Calculate **total revenue**
# Method 1: Using a loop
total_revenue = 0
for i in range(len(quantities)):
    revenue_per_sale = quantities[i] * prices[i]
    print(f"Sale {i+1}: {products[i]} - {quantities[i]} units x N{prices[i]} = N{revenue_per_sale}")
    total_revenue += revenue_per_sale

print(f"\nTotal revenue: N{total_revenue}")

# Method 2: Using zip (most elegant and Pythonic)
total_revenue_v2 = sum(q * p for q, p in zip(quantities, prices))
print(f"Total revenue (using zip): N{total_revenue_v2}")

