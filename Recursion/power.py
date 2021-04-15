base=int(input("Please Enter the base: "))
exp=int(input("Please enter the exp: "))
def power(base,exp):
    if exp == 0:
        return 1
    if(exp==1):
        return(base)
    if(exp!=1):
        return (base*power(base,exp-1))

print(power(base,exp))
