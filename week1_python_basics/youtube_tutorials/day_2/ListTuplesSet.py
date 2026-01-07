'''
we will begin learning about Lists, Tuples, and Sets in Python. 
Lists and Tuples allow us to work with sequential data, 
and Sets allow us to work with unordered unique values. 
We will go over most of the methods, learn when to use which data type, 
and also the performance benefits of each type as well. 
Let's get started.
'''

courses = ['histroy', 'math', 'pysics']
print(courses)
print(len(courses))

#indexing
print(courses[0])
print(courses[-1])#-1 will always have to be the last item on the list.
#slicing index
print(courses[0:3])
print(courses[:2])
print(courses[2:])
courses.append('english')
courses.append('igbo_language')#this add 'english to the 0 position
#using extend fuction
''' lets assume we have another list of courses and 
we want to add another list
;'''

courses_2 = ['french', 'chinese']
courses.extend(courses_2)# this will add the items on courses_2 list to the courses list.
print(courses)

'''when you use append to add the both list together it will append the courses_2 list 
into the contnet of courses list.like this 'histroy', 'math', 'pysics'  ['french', 'chinese']. 
instead of adding the individual items to the list. 
'''

courses.append(courses_2)
print(courses)

courses.remove('math') #this will remove math from the list
courses.pop()# this by default will remove the last item on the list
pooped = courses.pop()#this will reture the values removed from the list
print(pooped)
print(courses)
#we can reverse our list back the the way it way stating from the last item to the frist one
courses.reverse()
print(courses)
print(courses.sort())

num_list = [1, 5, 8, 7, 6, 0]
num_list.sort()
print(num_list)
'''you can also pass reverse fuction to the sort() 
to reverse the list from last to first
'''
courses.sort(reverse=True)
num_list.sort(reverse=True)
print(num_list)
print(courses)

print(sorted(courses))#this sort the list without altering with the content. it prints it how it is.


###tuples
# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)


# Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)


# Empty Lists
empty_list = []
empty_list = list()#built in

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()#built in empty tuples

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set() #built-in
#set does not care about order, it is use to check if an item is a member of a set, it does not support dulicate. discards the duplicated items. 
#we can also use sets to determine the items two sets has in common. 
cs_courses = {'histry', 'math', 'physics', 'compsci'}
art_courses = {'histry', 'math', 'art', 'design'}

print(cs_courses.intersection(art_courses))#this will print out the courses they have in common.
#you can also determing the items that are in a list but not in the other list
print(cs_courses.difference(art_courses))

#so to print the items combined we use the union() method
print(cs_courses.union(art_courses))
