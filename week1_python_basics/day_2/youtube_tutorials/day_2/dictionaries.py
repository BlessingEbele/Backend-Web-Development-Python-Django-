#we will begin learning about dictionaries. Dictionaries allow us to work with key-value pairs in Python. We will go over dictionary methods, how to add and remove values, and also how to loop through the key-value pairs. Let's get started.

student = {
    "name":"blessing",
    "age": 25,
    "courses": ['math', 'english', 'compsci']
}
print(student)

print(student['name'])
print(student['courses'])

print(student.get('name'))
print(student.get('phone'))# this will return 'none' by default, meaning the phone key doesn;t exist in the dictionary. 
# print(student['phone'])#this will throw a keyerror message becasue the dictionary doesn't have phone as a key

'''
we also set a defual error message to display if the key does not exist in a certain dictionary
by passing in the default error message that we want displayed
'''
print(student.get('phone', 'Not found'))
student['phone'] = '222-566-5565' #adding the phone key and value to the students dictionary

print(student)

#when we have a list of things to add to a dictinary we can use the update() method to do that. it takes dictionary as a list
student.update({'ocucupation': 'student', 'age': 32, 'hobbies': '(singing, dancing, skipping)'})
print(student)
#deleting a key from the dictionary

del student['hobbies']
print (student)

#we can uese pop() to remove a key 
age = student.pop('age')
print(student)
print(age)

#lenght
print(len(student))

#to see the keys
print(student.keys())

#to see the values
print(student.values())
#to see the kyes and the values
print(student.items())

#we can also loop through the kkey
for key in student:
    print(key)

#we can also loop for the key, value in the student dictionary
 for key, value in student.item():
    print(key, value)
    