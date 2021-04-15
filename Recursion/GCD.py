a=int(input("Please Enter the first number"))
b=int(input("Please Enter the second number"))

def GCD(a,b):
    assert int(a)==a and int(b)==b, "Please Enter a positive integer"
    if (a%b==0):
        return b
    
    if(a<0):
        a=-1*a
    if(b<0):
        b=-1*b 
    else:
        return GCD((int(b)),int(a%b))

print(GCD(a,b))