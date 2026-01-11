'''
��� Exercise 5 — Bonus (Challenge)
Create: bank.py
Simulate:
If balance > 500, print “You can withdraw.”


Else, print “Insufficient funds.”


Try adding a second condition:
 user_is_verified = True
'''

account_balance = 501
user_is_verified = False

if account_balance > 500 and user_is_verified:
    print('You can withdraw.')
elif account_balance <= 500:
    print('Insufficient funds.')
else:
    print('Account not verified. Please verify your account first.')