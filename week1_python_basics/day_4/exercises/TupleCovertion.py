'''
✅ Exercise 2 — Tuple Conversion
Take a list, convert to tuple, try modifying it (see error).
'''

countries = ["Ghana", "Japa", "Nigeria", "China", "Senegal"]# this is a list
print(f"the list: {countries}")
print(type(countries))

#Convert to tuple
countries_tuple = tuple(["Ghana", "Japa", "Nigeria", "China", "Senegal"])
print(type(countries_tuple))
print(f"the list converted to tuple: {countries_tuple}")

#try modifying
countries_tuple[0] = "USA" #this will rasie TypeError
