'''
 Exercise 1 — Work With Lists
Create a list of 5 countries:
Replace the 3rd country


Add 2 more


Remove the first item

'''
countries = ["Ghana", "Japa", "Nigeria", "China", "Senegal"]
print(f"Countries before manipulation: {countries}")

#replace the third country
countries[2] = "Chad"
print(f"Country after replacing the third country: {countries}")

#add 2 more
countries.append("Jamica")
countries.append("London")
print(f"Country after adding 2 more: {countries}")

countries.pop(0)
print(f"The result after removing the first country: {countries}")