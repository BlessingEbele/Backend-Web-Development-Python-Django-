'''
Challenge 10: Dictionary Looping

Create:
��� profile_loop.py

Given:

student = {
    "name": "Blessing",
    "age": 21,
    "course": "Backend Dev",
    "city": "Abuja"
}


Use a loop to print:

name : Blessing
age : 21
course : Backend Dev
city : Abuja


Concepts: looping through dictionary with .items()
'''

student = {
    "name": "Blessing",
    "age": 21,
    "course": "Backend Dev",
    "city": "Abuja"
}
for key, value in student.items():
    print(key, ":", value)

