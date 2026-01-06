#Here is a script combining all data types: 

#User profile 
name = "Blessing"
age = 31
score = 89.5
is_student = True 
hobies = ["coding", "reading", "traveling", "teaching","singing"]
profile = {
    "name": name,
    "age": age,
    "score": score, 
    "is_student": is_student,
    "hobies": hobies 
}
print(profile)
profile.update({"favorite_colors": "white"})

print(profile)

hobies.append("dancing")
print(hobies)
print(profile)
