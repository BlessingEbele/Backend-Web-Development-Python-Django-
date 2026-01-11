# COnditionals allow your program to make decisions. 
'''
mple in real life:
If it's raining → take umbrella


Else → go freely


In Python, this is written using:
if condition:
    do_something
elif another_condition:
    do_something_else
else:
    do_default_thing
'''
#simple innstruction statement

# tomorrow = 'saturday'
# yesterday = 'thursday'
# today = 'friday'

#getting input from user
# date = input(f'what day did the incident take place?:')

# if  date == today:
#     print("wow!, that was still fresh. i know it hurts but please take care of yourself.")
# elif date == yesterday:
#     print(f"'i was with them {yesterday} but still don't notice")
# elif date == tomorrow:
#     print(f"i'm pretty sure you already prepared for it")
# else:
#     print(f"i'm speechless")


#The if statememt + else statement
#Syntax: 
# condition = []
# if condition:
    #code runs when condition is true
 
 #example



# age = int(input('what is you age?: '))

# if age >= 18:
#     print("You are an adult.")
# else:
#     print("you are not an adult yet")

# #use else when you need a fallback option.
# age = int(input('what is your age?:'))

# if age >= 18:
#     print("You can vote.")
# else:
#     print("You cannot vote yet.")
# #Using elif for multiple conditions 

# #elif stands for “else if”.
# # 
# score = 75

# if score >= 80:
#     print("Excellent!")
# elif score >= 60:
#     print("Good job!")
# else:
#     print("You need to improve.")

# #Combining Conditions
# '''
# Use logical operators:
# Operator        Meaning
# and             both conditions must be True
# or              at least one condition must be True
# not             reverses True/False
# '''

# #Example:
# age = 25
# has_id = True

# if age >= 18 and has_id:
#     print("Entry allowed.")
# else:
#     print("Entry denied.")


# # Nested Conditionals

# # A conditional inside another conditional.

# age  = 19 
# has_ticket = False

# if age >= 18:
#     if has_ticket:
#         print('Welcome to the event')
#     else:
#         print('You Need a ticket')
# else:
#     print('You are too young.')

#EXample 2
age = 30
height = 3.6
is_female = True
is_pregnant = False
has_ticket = False

if age >= 18:
    print( ' you can ride the rollercoaster')
    if height <= 3.6:
        print('you are tall enough to ride the rollercoaster')
        if is_female and is_pregnant:
            print('unfortunately, pregnant women are not allowed to ride the rollercoaster for the safety of their unborn child(ren)')
        else:
            # print('pease get a ticket')there is no need add this. 
            if has_ticket:
                print('enjoy the rollercoaster')
            else: 
                print('please get a ticket')
        
    else:
        print('you need to grow more taller')
else:
    print('you are too young')


