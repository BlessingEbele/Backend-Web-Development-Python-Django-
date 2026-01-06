#Dictionaries store values using keys. 
person = {
    "name": "Blessing", 
    "age": 25, 
    "location": "Lagos"
}

print(person)

#Accessing values using keys:
print(person["name"])
print(person["age"])
print(person["location"])

#Adding new key-value pairs/new items:
person["job"] = "Engineer"
print(person)
person["profession"] = "Translator"
print(person)

#Removing items:
del person["age"]
print(person)
 
#Checking if a key exists:
if "name" in person:
    print("Name is a key in the dictionary")
else:
    print("Name is not a key in the dictionary")

if "age" in person: 
    print("Age is a key in the dictionary")
else:
    print("Age is not a key in the dictionary")

#Getting all keys:
print(person.keys())


#Getting all values:
print(person.values())
