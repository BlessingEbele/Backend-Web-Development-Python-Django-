'''
# ��� Python Code Challenge 2: Sales & Inventory Analyzer

## ��� Scenario

You’re building a **simple inventory and sales analyzer** for a small shop.

Each product has:

* a name
* quantity sold
* unit price

You’ll analyze performance using **lists, tuples, sets, integers, and operators**.

---

## ��� Given Data

```python
products = ["rice", "beans", "yam", "rice", "beans", "oil", "yam"]
quantities = [10, 5, 8, 6, 7, 3, 2]
prices = [500, 300, 200, 500, 300, 1000, 200]
```

> Each index represents **one sale**
> Example: `"rice", 10, 500` → 10 bags of rice sold at ₦500 each

---

## ��� Tasks

### 1️⃣ List & Integer Operations

* Calculate **total items sold**
* Calculate **total revenue**

---

### 2️⃣ Set Operations

* Extract **unique products**
* Count how many **different products** were sold

---

### 3️⃣ Tuple Operations

Create a tuple for **each sale** in this format:

```python
(product_name, quantity, price, revenue)
```

Store all tuples in a list.

---

### 4️⃣ Operator & Conditional Logic

* Count how many sales generated **revenue greater than ₦3000**
* Apply a **10% discount** to sales where quantity ≥ 8
* Use comparison and arithmetic operators

---

### 5️⃣ Membership & Logical Operators

* Check if `"oil"` was sold
* Check if `"salt"` was sold
* Use `and` / `or` at least once

---

## ��� Bonus (Optional)

* Find the **highest revenue sale**
* Sort sales by revenue (highest → lowest)
* Use a **ternary operator** for discount logic

---

## ��� Rules

❌ No external libraries
❌ No AI autocomplete
✅ Clean Python only

---

## ��� Instructions

1️⃣ Write your solution **from scratch**
2️⃣ Test it in your editor
3️⃣ Paste your full code here
4️⃣ I’ll review it **line-by-line** like before

Take your time — quality over speed ���
When ready, paste your solution and say:

> **“Here is my solution”**

You’ve got this ���
'''
products = ["rice", "beans", "yam", "rice", "beans", "oil", "yam"]
quantities = [10, 5, 8, 6, 7, 3, 2]
prices = [500, 300, 200, 500, 300, 1000, 200] 

# 1️⃣ List & Integer Operations

#Calculate **total items sold
TotalItemSold = sum(quantities)
print(f"Total item sold: {TotalItemSold}")

'''
to Calculate the total revenue multiply the 
Quantity Sold by the Price Per Unit,
 using the formula: Total Revenue = Quantity Sold x Price Per Unit; 
 for businesses with multiple products or services, 
 calculate revenue for each and sum them up, 
 adjusting for returns or discounts to get net revenue. 
 This simple formula provides the gross income before deducting costs, 
 showing total money earned from sales over a specific period. 
 Basic Calculation (Single Product) Identify Quantity: Count the total number of units sold (e.g., 1,000 t-shirts).Determine Price: Find the price for each unit (e.g., $10 per t-shirt).Multiply: \(1,000\text{\ units}\times \$10/\text{unit}=\$10,000\text{\ Total\ Revenue}\). For Multiple Products/Services (Gross Revenue) Calculate the revenue for each product/service individually and then add them together.Example: A company sells 500 phones at $800 each and 200 laptops at $1,200 each.Phones: \(500\times \$800=\$400,000\)Laptops: \(200\times \$1,200=\$240,000\)Total Gross Revenue: \(\$400,000+\$240,000=\$640,000\). Calculating Net Revenue (After Adjustments) Start with your gross revenue and subtract returns, allowances, and discounts.Formula: Total Revenue = (Quantity Sold x Unit Price) - Discounts - Returns. 
 '''
# TotalRevenue = Quantity Sold x Price Per Unit

total_revenue = 0
for i in range(len(quantities)):
    total_revenue += quantities[i] * prices[i]
print(f"Total revenue: N{total_revenue}")

# 2️⃣ Set Operations
#Extract unique products
unique_products = set(products)
print(f"Unique products: {unique_products}")

#count different products
different_products_count = len(unique_products)
print(f"Number of different products: {different_products_count}")


# 3️⃣ Tuple Operations
#create tuple for each sale; (product_name, quatity, price. revenue)
sales_tuples = []
for i in range(len(products)):
    revenue = quantities[i] * prices[i]
    sale_tuple = (products[i], quantities[i], prices[i], revenue)
    sales_tuples.append(sale_tuple)
print("\nSales Tuples:")

for sale in sales_tuples:
    print(sale)


# 4️⃣ Operator & Conditional Logic
#count sales with revenue > N3000
high_revenue_count = 0
for sale in sales_tuples:
    if sale[3] > 3000:  #sale[3] is revenue
        high_revenue_count += 1
print(f"\nSales with revenue > 300: {high_revenue_count}")

#Apply 10% discount to slaes where quantity >= 8
print("\n Sales with 10% discount (quantity >= 8):")
for sale in sales_tuples: 
    if sale[1] >= 8: #sales[1] quantity
        discounted_revenue = sale[3] * 0.9  #10% discount
        print(f"{sale[0]}: original N{sale[3]}, Discounted N{discounted_revenue}")


# 5️⃣ Membership & Logical Operators
#check if "oil" was sold
oil_sold = "oil" in products
print(f"Was oil sold? {oil_sold}")

#check if "salt" was sold
salt_sold = "salt" in products
print(f"Was salt sold? {salt_sold}")

#Using and/or operators
if oil_sold and not salt_sold:
    print("Oil was sold but salt was not sold")

#Bonus
#find highest revenue sale
highest_revenue_sale = sales_tuples[0]
for sale in sales_tuples:
    if sale[3] > highest_revenue_sale[3]:
        highest_revenue_sale = sale
print(f"\nHighest revenue sale: {highest_revenue_sale}")

#sort slaes by revenue (highest to lowest)
sorted_sales = sorted(sales_tuples, key=lambda x: x[3], reverse = True)
print("\nSales sorted by revenue(highest to lowest): ")
for sale in sorted_sales:
    print(sale)

#Ternary operator for discount logic
print("\nUsing ternary operator for discount:")
for sale in sales_tuples:
    final_revenue = sale[3] * 0.9 if sale[1] >= 8 else sale[3]
    discount_status = "with discount" if sale[1] >= 8 else "no discount"
    print(f"{sale[0]}: N{final_revenue} ({discount_status})")

'''
Key Points Explained:
1️⃣ Total Revenue Calculation:

Loop through each index
Multiply quantities[i] * prices[i]
Add to running total
2️⃣ Set for Unique Products:

set(products) automatically removes duplicates
3️⃣ Tuples:

Create a tuple for each sale with 4 elements
Store in a list
4️⃣ Conditional Logic:

Use if statements to check conditions
Access tuple elements by index: sale[3] for revenue
5️⃣ Membership Operators:

in checks if item exists in list
and/or combine conditions
Bonus:

Ternary: value_if_true if condition else value_if_false
sorted() with key parameter sorts by specific element
'''