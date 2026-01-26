'''
Challenge 5: Fixed Student Record (Tuples)

Create:
��� student_tuple.py

Create a tuple:

student = ("Blessing", 20, "Backend Dev")


Print:

The student’s name

The course

Then add a comment explaining why you cannot change the age.

Concepts: tuple access + immutability
'''

student = ("Blessing", 20, "Backend Dev")
print(f"The student name: {student[0]}")
print(f"The course: {student[2]}")
print("Tuple is immutable and therefore the data can't be altered or changed")
