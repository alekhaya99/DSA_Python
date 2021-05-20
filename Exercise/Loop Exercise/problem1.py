'''
Question1: 
 Ask the user for two numbers between 1 to 100 and print the count from the lower number to the upper number
'''

num1=int(input("Please enter the 1st number between 1 to 100: "))
num2=int(input("Please enter the 2nd number between 1 to 100: "))

while num1>100 or num2>100 or num1==num2 or num1<0 or num2<0:
    num1=int(input("Please enter the 1st number between 1 to 100: "))
    num2=int(input("Please enter the 2nd number between 1 to 100: "))

if num1>num2:
    for i in range (num2,num1+1):
        print (i,end=' ')
else:
    for i in range (num1,num2+1):
        print (i,end=' ')