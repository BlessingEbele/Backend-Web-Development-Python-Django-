# string represents text surrounded by quotes ("")

message = "Welcome to python!"

print(message)

#string operations:
#concatenation (joining strings)

first_name = "Blessing"
last_name = "Anochili"
full_name = first_name + " " + last_name
print(full_name)

#lenght of a string
print(len(full_name))
print(len(first_name))
print(len(last_name))
print(len(message))


print("The lenght of the full name is:", len(full_name))
print("The lenght of the last name is:", len(last_name))
print("The lenght of the fisrt name is:", len(first_name))
print("The lenght of the message is:", len(message))


#changing case of a string

print(full_name.upper())
print(full_name.lower())
print(full_name.title())
