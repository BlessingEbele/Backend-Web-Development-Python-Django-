'''
��� Exercise 3 — Login System
Create: login.py
Store correct username & password


Ask user to input theirs


Validate using if/else

'''

Username = 'cynthia'
password = '1235'

Entered_Username = input("Enter your username: ")
Entered_password = input('Enter your password: ')

if Entered_Username == Username and password == Entered_password:
    print('Login Successful')
else: 
    print('Invalid username or password')