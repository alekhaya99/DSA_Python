'''
Problem3:
Ask the user to enter a number between to 1 to 13 and display a table of that number 
'''

number=input("Please enter a number between 1 to 13: ")

while (not number.isdigit()) or (int(number)<1 or int(number)>13):
    number=input("Please enter a number between 1 to 13: ")

number=int(number)

for i in range(0,14):
    print(f'{i} * {number} = {i*number}')