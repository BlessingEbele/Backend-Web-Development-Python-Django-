'''
✅ Exercise 4 — Dictionary Practice
Create a dictionary for a product with:
name
price
quantity
Then:
update the price
add a "category"
print all keys and values
'''

product_dictionary = {
    "name": "grape juice",
    "price": 150,
    "quantity" : 100,
}

#update 
product_dictionary["price"] = 200
product_dictionary["category"] = "fruit juice"
print(f"the new product: {product_dictionary}")

for key, value in product_dictionary.items():
    print(key, ":", value)