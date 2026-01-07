# working with Numeric data in python

num = 3
print(type(num))
num = 3.14 
print(type(num))
# we can do both addition, subtraaction, division, multiplication using +,-,/,* respectively.
print(3/2)# this will give you 1.5 we can round it up to whole number by perfoeming floor division using //. it will eliminate the remiander.
print(3//2)

print(3 ** 2) #exponet
print(3 % 2) #modulus

print(3 * 2 + 1)
print(3 * (2 + 1))# using parentesis to tell the computer which operation to run first

#number incremetation
num = 1
num += 1 #this will increse the number by 1
print(num)

num *= 10 #this will multiply the number by 10
print(num)
'''
this is just like saying 
num *= n (where n stands for a particular numner) 
for example
num *= n this will multipy the number by n raise to the number 

num = 5
num *= 6 is 5*6
lets ee it in action.
'''
num = 5
num *= 6
print(num)
print(abs(-3)) # the absolute vale of -3 will be printed out
print(round(3.78)) #this rounds 3.78 to a whole number which is 4
print(round(3.78, 1)) # this is passing of an argument telling the computer to round the nume to one decimal place. which will now give 3.8 instaed. 
#another use example is 
print(round(3.4567, 2)) # this will print out 3.46 to the console. leaving the number to two decila palces. 

#the use of comparision in python
'''
egauls: 6 == 2
not equal: 6 != 2
greater than: 3 > 2
less than: 3 < 2
greater or equal: 3 >= 2
less or equal: 3 <= 2
'''

num_1 = 3
num_2 = 2

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

num_1 = '100'
num_2 = '200'
print(num_1 + num_2) # this will concatenate the value and print it out as string.
''' to print the result out as an integer we convert the 
 to integer using 'int'
'''
num_1 = int(num_1)
num_2 = int(num_2)

#now it add the numbers together and print the resul out as integer

print(num_1 + num_2)
