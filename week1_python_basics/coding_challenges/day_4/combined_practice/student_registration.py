'''
Challenge 1: Student Registration System

Create a file:
��� student_registration.py

Requirements:

Store student details using variables:

name (string)

age (integer)

is_registered (boolean)

Store courses in a list:

courses = ["Python", "Git", "Backend Basics"]


If the student is registered:

Print the student's name

Print the list of courses

Else:

Print "Please complete your registration"

Concepts tested: variables, booleans, lists, if/else
'''
name = "Blessing"
age = 30
is_registered = True

courses = ["Python", "Git", "Backend Basics"]

if is_registered == True:
    print(f"{name}: course {courses}")
else:
    print("Please complete your registration")
    