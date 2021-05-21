n=int(input("Please enter a number: "))
a=[]

def Fibbonaci(n):
    assert n>=0 and int(n)==n, "Please enter a positive integer"
    if n in [0,1]:
        return n
    else:
        b=Fibbonaci(n-1)+Fibbonaci(n-2)
        return b
        
        

print(Fibbonaci(n))

print("Fibonacci sequence:")
for i in range(n):
    print(Fibbonaci(i),end=" ")