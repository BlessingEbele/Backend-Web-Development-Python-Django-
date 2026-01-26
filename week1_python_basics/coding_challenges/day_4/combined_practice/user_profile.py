'''
Challenge 3: User Profile Manager

Create:
�� user_profile.py

Create a dictionary:

user = {
    "username": "blessing_dev",
    "age": 22,
    "city": "Lagos"
}


Tasks:

Print the username

Update the age

Add a new key "skills" with a list of skills

Use an if statement:

If age is 18 or above → print "Adult user"

Else → print "Minor user"

Concepts tested: dictionary, list inside dict, modification, if/else 
'''

user = {
    "username": "blessing_dev",
    "age": 22,
    "city": "Lagos"
}
print(user["username"])
user["age"] = 32
user["skills"] = ["coding", "writing"]

if user["age"] >= 18:
    print("Adult user")
else:
   print("Minor user")

print(user)
