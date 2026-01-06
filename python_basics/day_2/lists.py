#List can store multiple items. 

shopping_list = ["milk", "bread", "eggs"]
print(shopping_list)

print(type(shopping_list))
print(len(shopping_list))


#Accessing items:
print(shopping_list[0]) #this will list the first item on the list 

#adding items to the list:
shopping_list.append("butter")
print(shopping_list)

#changing items on the list:
shopping_list[1] = "whole bread"
print(shopping_list)

shopping_list.remove("milk")
print(shopping_list)

shopping_list.sort()
print(shopping_list)

print(len(shopping_list))
print(type(shopping_list))
