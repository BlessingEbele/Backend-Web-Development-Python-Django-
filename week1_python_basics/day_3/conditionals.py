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



age = int(input('what is you age?: '))

if age >= 18:
    print("You are an adult.")
else:
    print("you are not an adult yet")

#use else when you need a fallback option.
age = int(input('what is your age?:'))

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")
