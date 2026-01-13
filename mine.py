��� Python Code Challenge 2: Sales & Inventory Analyzer

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
print(TotalItemSold)
#total revenue

# revenue = {
#     TotalRiceSold == quantities[0] * prices[0]
#}

# print({products[0]})
# print(TotalRiceSold)
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