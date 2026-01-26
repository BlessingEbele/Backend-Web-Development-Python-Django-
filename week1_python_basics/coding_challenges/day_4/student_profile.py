'''
Challenge 9: Student Profile (Dictionary)

Create:
��� student_profile.py

Create a dictionary with:

name

age

course

Then:

Print the name

Update the age

Add a new key: "city"

Print the full dictionary

Concepts: dictionary access + modification
'''
student_profile = {
    "name": "Blessing",
    "age":30,
    "course": "computer science",

}
print(f"student name: {student_profile['name']}")

student_profile["city"] = "Abuja"
student_profile["age"] = 32

print(f"The student profile: {student_profile}")