'''
Challenge 5: Backend Access Control (Real-world logic)

Create:
��� access_control.py

Given:

user = ("Blessing", "admin")   # tuple (name, role)


Tasks:

Extract the name and role from the tuple

If role is "admin" → print "Full system access granted"

If role is "editor" → print "Limited access granted"

Else → print "View only access"

Concepts tested: tuples, variables, conditionals, backend-style logic
'''
user = ("Blessing", "admin")   # tuple (name, role)
name = user[0]
role = user[1]

if role == "admin":
    print("Full access")
elif role == "editor":
    print("Limited Access")
else:
    print("View only")
    