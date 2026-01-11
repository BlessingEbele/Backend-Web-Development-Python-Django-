#Combining Conditions
'''
Use logical operators:
Operator        Meaning
and             both conditions must be True
or              at least one condition must be True
not             reverses True/False
'''

#Example:
age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")
else:
    print("Entry denied.")

