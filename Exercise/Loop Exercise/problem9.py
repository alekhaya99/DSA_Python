'''
Question 9:  Label the count of the particular number as odd and even
'''

n=int(input("Please enter a number"))
odd_no=[]
even_no=[]

for i in range(1,n+1):
    if i%2==0:
        even_no.append(i)
    else:
        odd_no.append(i)

print(f'The odd numbers are {odd_no}')
print(f'The even numbers are {even_no}')