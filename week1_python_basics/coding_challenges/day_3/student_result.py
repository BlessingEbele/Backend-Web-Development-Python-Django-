'''
��� MINI PROJECT (Week 1 – Conditionals)
��� Project Title: Student Result Checker
��� Project Goal

Build a small Python program that:

Collects a student’s score

Uses decision-making (if / elif / else)

Assigns a grade

Gives feedback
Just like a real school system.

��� Project Scenario

You are building a simple backend logic for a school portal.
When a student submits their score, the system should:

Determine their grade

Display a performance message

��� Project Requirements

Create a file called:

student_result.py


Your program should:

Store a student's name

Store a student's score (0–100)

Use conditions to assign grades:

Score Range	Grade
70 – 100	A
60 – 69	B
50 – 59	C
40 – 49	D
Below 40	F

Print output like:

Student: Blessing
Score: 78
Grade: A
Excellent performance!

�� Feedback Rules

Grade A → "Excellent performance!"

Grade B → "Very good, keep it up!"

Grade C → "Good, you can improve."

Grade D → "Try harder next time."

Grade F → "You need to work much harder."


⭐ Bonus Challenge (For Fast Learners)

Ask learners to extend the project:

Add another condition:

If score is above 100 or below 0 → print
"Invalid score entered"

That introduces validation logic (very important in backend development).
'''

student_name = str(input("Enter your name: "))
student_score = int(input("Enter your score: "))
print(f"Student: {student_name}")

# Validate score first
if student_score < 0 or student_score > 100:
    print(f"Score: {student_score}\nInvalid score entered.")
elif student_score >= 70:
    print(f"Score: {student_score}\nGrade: A\nExcellent performance!")
elif student_score >= 60:
    print(f"Score: {student_score}\nGrade: B\nVery good, keep it up!")
elif student_score >= 50:
    print(f"Score: {student_score}\nGrade: C\nGood, you can improve.")
elif student_score >= 40:
    print(f"Score: {student_score}\nGrade: D\nTry harder next time.")
else:
    print(f"Score: {student_score}\nGrade: F\nYou need to work much harder.")