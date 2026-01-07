message = 'hello world'
print(message)
print(message.count('hello'))# here the word hello apear once in our 'message'
print(message.count('l'))#L appears more than once
print(message.upper())
print(message.lower())
print(message.find('universe'))# this will ruture negative 1 (-1) because the word'universe' is not the the message
print(message.replace("world","universe"))# here the word 'world' will be repalced with the word 'universe'


greeting = 'hello'
name = 'blessing'
message = greeting + ', ' + name + '. Welcome!'
print(message)
message = '{}, {}. welcome!'.format(greeting, name)
print(message)
message = f'{greeting}, {name}. welcome'
print(message)


print(dir(name))#this will give all the attributes and methods that we can access to using the name variable. 

print(help(str))# this will give use a description of what these methods do and what arguments they take. 
'''
 so if we have a mothod but do not remember what its does, we can pass help to that method to see mroe inforamtion about the the method or function. 
 for example we can check what.lower()method does
'''
print(help(str.lower)) #this will give you the overview of the str.lower() method.
