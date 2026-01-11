'''
Exercise 2 — Temperature Checker
Create: weather.py
If temperature is:
30 → “Too hot!”



20–30 → “Warm”


10–19 → “Cold”


< 10 → “Very Cold!”


'''

Temperature = 31


if Temperature < 10:
    print('Very cold!')
elif Temperature >= 10 and Temperature <= 19:
    print('Cold')
elif Temperature >= 20 and Temperature <= 30:
    print('Warm')
else:
    print('Too hot!')