''' A function is a reusable block of code used to perform a specific task.
Why use functions?
Avoid repeating code


Organize your program better


Make code cleaner and easier to maintain


Improve reusability
'''
#Defininn a fuction
# def fuction_name():
    #code block


#example 
def greet():
    print("Hello, welcome to python!")

#calling the fuction
greet() #this will actually print the block of code after defining the fuction. meaning it can only be printed when called

'''
note that Function names follow the same rules as variable names in Python:

A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)
'''
#example 
'''
Valid function names:

calculate_sum()
_private_function()
myFunction2()
'''
#Functions with Parameters
#Parameters allow you to send information into a function.
#Example
def greet(name):
    print(f"Hello {name}, How are you?")

greet("Blessing")
greet("Bliss")
greet("Nkechi")
#Functions with Multiple Parameters
def add(a, b):
    print(f"The sum of the integers is: {a + b}")

add(3, 5)

# Functions That Return a Value
'''
Functions can send data back to the code that called them using the return statement.

When a function reaches a return statement, it stops executing and sends the result back:

'''
#Example

#Use return to send a value back from a function.
def multipy(a, b):
    return a * b
result = multipy(4, 6)
print("Result:", result)

def get_greeting():
  return "Hello from a Blessing's Fuction"

message = get_greeting()
print(f"The mesaage: {message}")

#you can use the return valu diirectly
def get_greeting():
  return "Hello from a Blessing's  function"

print(get_greeting())

def multiply():
    return "a * b"
# result = multipy(4, 6)
print(multiply())

'''
Return vs Print
print() → displays something


return → gives back a value so you can use it later
'''
#Example:
def square(n):
    return n * n

value = square(5)
print(value)

# Default Parameters

#Useful when you want a function to have optional values.
def greet(name="friend"):
    print("Hello", name)

greet()
greet("Ada")
