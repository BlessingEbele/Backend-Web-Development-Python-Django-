'''
Challenge 7: Unique Names (Sets)

Create:
��� unique_names.py

Given:

names = ["John", "Mary", "John", "Aisha", "Mary"]


Convert the list to a set and print the unique names.

Concepts: removing duplicates using set



'''

names = ["John", "Mary", "John", "Aisha", "Mary"]

unique_names = set(names)
print(type(unique_names))
print(f"Unique names: {unique_names}")