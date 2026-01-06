'''
��� Exercise 3 — Student Dictionary
Create a file: student.py
Include:
name


id_number


grades list


dictionary of contact info


Print the student dictionary in a neat format.
'''

name = "Blessing"
id_number = 548763155
grades = ["c", "a", "a", "b"]
grade2 = {"math": "c", "english": "a", "history": "a", "science": "b"}

data = {
    "name":name,
    "id_number":id_number, 
    "grades": grades,
    "grade2":grade2

}
# print(contacts)


contact_info = {
    "email": "blessmart.com@gmail.com",
    "phone": "+234814095685",
    "linkedil":"www.linkedil.com/blessingebele",
    "github":"www.github.com/blessingebele",
    "Home_address": "no 1 eze street" ,
    "nationality": "china"
}
# print(contact_info)
print("your contact information is:", (contact_info))
print("your data is:", (data))

