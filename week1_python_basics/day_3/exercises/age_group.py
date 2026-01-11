'''
��� Exercise 4 — Age Group Classifier
Create: age_group.py
Rules:
0–12 → Child


13–19 → Teen


20–35 → Young Adult


36–60 → Adult


60+ → Senior



'''

age = 61


if age >= 0 and age <= 12:
    print('you are a child')
elif age >= 13 and age <= 19:
    print(' you are a teen')
elif age == 20 or age <= 35:
    print('Young adult')
elif age == 36 or age <= 60:
    print('you are an adult')
# elif age <= 60:
else:
    print(' you are a senior')
# else:
    # print('you will leave longer')


#another way

age = int(input('what is your age:?'))

if age >= 0 and age <= 12:
    print('you are a child')
elif age >= 13 and age <= 19:
    print(' you are a teen')
elif age >= 20 or age <= 35:
    print('Young adult')
elif age >= 36 or age <= 60:
    print('you are an adult')
# elif age <= 60:
else:
    print(' you are a senior')
# else:
    # print('you will leave longer')

#OR
age = int(input('how old are you?: '))

if age < 0:
    print('invalid age')
elif age <= 12:
    
    print('you are a child')
elif age <= 19:
    print(' you are a teen')
elif age <= 35:
    print('Young adult')
elif age <= 60:
    print('you are an adult')
# elif age <= 60:
else:
    print(' you are a senior')
# else:
    # print('you will leave longer')