'''
Question 5: Calculate an factorial
'''

n=int(input("Please enter a number: "))
fact=1

for i in range (1,n+1):
    fact=i*fact

print(fact)
