'''
Challenge 7: Temperature Advisor

Create:
��� weather.py

Store:

temperature = 30


Rules:

If above 35 → "It's too hot"

If between 25 and 35 → "The weather is warm"

Else → "It's cold"

Concept: Range checks
'''
temperature = 24
if temperature >= 35:
    print("It's too hot")
elif temperature >= 25 and temperature  <= 34: 
    print("The weather is warm")
else: 
    print("It's cold")