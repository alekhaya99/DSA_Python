'''
Question6: Print a Fibbonaci Series

'''

n=int(input("Please Enter a number: "))
fib_num=[]

for i in range(n):
    if i==0:
        fib_num.append(0)
    elif i==1:
        fib_num.append(1)
    else:
        a=fib_num[(i-1)]+fib_num[(i-2)]
        fib_num.append(a)

print(fib_num)