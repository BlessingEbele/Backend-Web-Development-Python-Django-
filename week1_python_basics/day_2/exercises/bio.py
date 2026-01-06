#📝 Exercise 1 — Create a Simple Bio
'''Create a file: bio.py
Include:
Name


Age


A boolean (e.g., has_children)


A list of hobbies


Print them one by one.
'''


name = "Blessing"
age = 31
has_children = True
hobbies = ["coding", "reading", "traveling", "teaching","singing"]

data = {
    "name": name,
    "age": age,
    "has_children": has_children,
    "hobbies": hobbies
}
print(data)
print(type(data))

print(data["name"])
print(data["age"])
print(data["has_children"])
print(data["hobbies"])
data.remove("hobbies"])
print(data)
