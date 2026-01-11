# Test all temperature ranges

test_temps = [5, 10, 15, 19, 20, 25, 30, 35]

for temp in test_temps:
    print(f"Temperature = {temp}: ", end="")
    if temp < 10:
        print('Very cold!')
    elif temp >= 10 and temp <= 19:
        print('Cold')
    elif temp >= 20 and temp <= 30:
        print('Warm')
    else:
        print('Too hot!')
