'''
Challenge 3: Number Slicing

Create:
��� slicing.py

Given:

numbers = [10, 20, 30, 40, 50, 60]


Print:

The first three numbers

The last three numbers

The middle two numbers (30, 40)

Concepts: list slicing
'''
numbers = [10, 20, 30, 40, 50, 60] 
print(f"The first three numbers are:{numbers[:3]}")
print(f"The last three numbers are : {numbers[3:]}")
print(f"The middle two numbers are: {numbers[2:4]}")
