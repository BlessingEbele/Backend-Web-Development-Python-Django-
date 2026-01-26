'''
Challenge 2: Shopping Cart Checker

Create:
��� shopping_cart.py

Given:

cart = ["rice", "beans", "oil", "rice", "beans"]


Tasks:

Convert the cart to a set to remove duplicates

Print the unique items

If "oil" is in the cart → print "Item available"

Else → print "Item not available"

Concepts tested: lists, sets, duplicates, conditionals '
'''

cart = ["rice", "beans", "oil", "rice", "beans"]
cart_set = set(cart)
print(f"The unique items: {cart_set}")

if "oil" in cart_set:
    print("Item available")
else:
    print("Item not available")
