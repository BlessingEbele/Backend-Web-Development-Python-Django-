'''
Challenge 5: Grade Checker

Create:
��� grade.py

Store a score:

score = 75


Rules:

If score ≥ 70 → A

If score ≥ 60 → B

If score ≥ 50 → C

Else → F

Print the grade.

Concept: if / elif / else
'''
score = 65
if score >= 70:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Fail")