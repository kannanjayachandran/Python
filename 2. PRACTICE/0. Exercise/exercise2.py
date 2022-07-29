#  EXERCISE 2

'''
Question 1

Using a dictionary containing countries and their capitals; write a program 
that asks the user to input a country and check if the country is present in 
the dictionary if present print the capital of the country if not then print no.
'''

capital_dict = {'India': 'New delhi', 'France': 'Paris',
                'Afganistan': 'Kabul', 'United Kingdom': 'London', 'Italy': 'Rome'}

p = input("Enter the country name: ")

# Checking for edge cases.
while 'united kingdom' not in p.lower() and not p.isalpha():
    print("Input a string")
    p = input("Enter the country name: ")

p = p.lower().title()

if p in capital_dict.keys():
    print(f'The capital of {p} is {capital_dict[p]}')
else:
    print("Country is not available")
