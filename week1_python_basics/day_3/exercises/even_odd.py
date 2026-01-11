'''
Requirements:
Ask user for a number


If number is even → print "Even"


Otherwise → print "Odd"


Hint:
if number % 2 == 0:
'''

number = int(float(input('Enter a number: ')))# this line can take both floating number and int because it coverts the input to both float and int ant work with them both.
number = int(input('enter a number: '))#this line of code caanot take a floating number as input. it only convert the input to int and work with int.
if number % 2 == 0:
    print('even number')
else:
    print('Odd number')
