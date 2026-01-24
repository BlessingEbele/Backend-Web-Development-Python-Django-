'''
✅ Exercise 3 — Set Operations
Given two sets:
Find common items


Find items only in the first set
'''
names = {"Blessing", "Nora", "Eunice"}
age = {23, 45, 25}
names2 = {"James", "Blessing", "Chike"}
age2 = {23, 34, 67}

print(f"The u ion of first name and the second name: {names.union (names2)}") 
print(f"The union of the first age and the second age: {age.union(age2)}")
print(f"The Difference between the first age and the second age: {age.difference(age2)}")
print(f"The Difference between the first name and the second name:{names.difference(names2)}")

#find the common item
print(f"The interserction of the first age and the second age:{age.intersection (age2)}")# what they have in common 
print(f"The intersection of the first name and the second name:{names.intersection(names2)}")# what they have in common


