# Nested Conditionals

# A conditional inside another conditional.

age  = 19 
has_ticket = False

if age >= 18:
    if has_ticket:
        print('Welcome to the event')
    else:
        print('You Need a ticket')
else:
    print('You are too young.')

#EXample 2
age = 30
height = 3.6
is_female = True
is_pregnant = False
has_ticket = False

if age >= 18:
    print( ' you can ride the rollercoaster')
    if height <= 3.6:
        print('you are tall enough to ride the rollercoaster')
        if is_female and is_pregnant:
            print('unfortunately, pregnant women are not allowed to ride the rollercoaster for the safety of their unborn child(ren)')
        else:
            # print('pease get a ticket')there is no need add this. 
            if has_ticket:
                print('enjoy the rollercoaster')
            else: 
                print('please get a ticket')
        
    else:
        print('you need to grow more taller')
else:
    print('you are too young')


