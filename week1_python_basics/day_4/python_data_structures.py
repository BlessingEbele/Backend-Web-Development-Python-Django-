'''
Python Data Structures (Lists, Tuples, Sets, Dictionaries)
Goal: Understand and work with Python's built-in data structures, when to use each one, and how to manipulate them confidently.

'''
#lists
#creating lists
fruits = ["apple", "banana", "oranges"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 7, True]
print(f"Fruits before manipulations: {fruits}, \nNumbers before manipulations: {numbers}, \nMixed before manipulations: {mixed}")

#list operations
fruits.append("mango") # this adds mango to the end of the fruits list
fruits.insert(1, "kiwi") # this will insert kiwi at index 1
fruits.remove("banana") # this removes banana from the list of items
fruits.pop() # this removes the last item on the list
fruits.pop(1)# this removes item on the index 1

print(f"Fruits after manipulations {fruits}")

# Accessing the items in the list
print(fruits[0]) # this will print the first item on the list
print(fruits[-1]) #this will always print the last item on the list regardless of the number of items on that list.


# List slicing
numbers = [1, 2, 3, 4, 5, 6] 
print(numbers[1:4]) # [2, 3, 4] this will print items in the list starting fro the second item down to the forth item. the first item on the list is always labelled 0(zero)
print(numbers[:3]) # [1, 2, 3] this will print from the first item through thr third item on the list
print(numbers[3:]) #[4, 5, 6] this will print from the third item to the last item. 

#note, when we pass the parameters [:3]  and [3:] it simply mean that the prongram will display from the first item on the list to the third and from the third item to the last item respectively

#Tuples
#tuples are immutable- they can can't be altered
#creating tuples
person = ("john", 25, "Lagos")
coords = (10.5, 20.3)

#Accessing Tuples

print(f"person: {person}")
print(f"person index 0: {person[0]}") 

#trying to change the date
#person[1] = 30 # this will throw an error! can't modifiy (TypeError).'tuple' object does not support item assignment


#Sets
# A set is an unordered collection of unique items.
#it dosen't care about the order and do not support duplicated items in a set

#Creating sets
colors = {"red", "blue", "green" }

#Removing duplicates
colors = {"red", "blue", "green",  "yellow", "green"}
nums = {1, 1, 2, 3, 4, 4}
print(colors) # {'red', 'blue', 'yellow', 'green'}
print(nums)  # {1, 2, 3, 4}

#Useful Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(f"the union of a and b is : {a.union(b)}")        # {1, 2, 3, 4, 5} the unites a and b together and print the result.
print(f"the intersection of a and ab {a.intersection(b)}") # {3} this shows what a and b has in common
print(f"the difference btw a and b is :{a.difference(b)}")   # {1, 2} this shows the difference btw a and b

#Dictionaries (Key-Value Pairs)
#dictionaries store data in key -- Value format.

#Creating Dictionaries
student= {
    "name": "Blessing", 
    "age": 20,
    "course": "Backend Dev."
}
print(f"The student is :{student}")

#Accessing Values
print(student["name"])
print(student.get("course"))
print(student["course"])
print(student.get("name"))

#Modifying Dictionaries
student["age"] = 21
student["city"] = "Abuja"
print(f"the student updated data: {student}")

#Looping Through a Dictionary
for key, value in student.items():
    print(key, ":", value)
for key in student.keys():
    print(f"the keys: {key}")

    