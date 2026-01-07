#Tuples are like lists but cannot be modified. 
colors = ("red", "blue", "green")
print(colors[0])

#Trying to modify: 
# colors[0] = "yellow" #This causes an error

print(type(colors))
print(len(colors))
colors.append("white", "black") #this will run into error. 
print(colors)
