'''
Challenge 10: Backend Access Level

Create:
�� access_level.py

Store:

role = "admin"


Rules:

If admin → "Full access"

If editor → "Limited access"

Else → "View only"

Concept: Role-based decision logic (real backend concept)

'''

role = "editor"
if role == "admin":
    print("Full access")
elif role == "editor":
    print("Limited access")
else:
    print("View only")



