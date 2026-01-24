'''
Mini-Project of the Day — “Student Record System”
Requirements
Create a dictionary representing a student.
The student has:
name
age
list of courses
a nested dictionary for scores
Add a new score
Print the highest score

'''
student = {
    "name": "Blessing",
    "age": 30,

    "list of courses" :["information technology", "anatomy"],
    "scores": {
        "information technology": 80,
        "anatomy": 95,
    }
}

student["scores"]["computer technology"]= 85
print("Student Record:", student)
print("Highest score: ", max(student["scores"].values()))