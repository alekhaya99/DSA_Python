n=int(input("Please eneter a number: "))

def Sum_of_no(n):
    assert n>=0 and int(n)==n, "Please enter a positive integer "
    if n==0:
        return 0
    else:
        return int(n%10)+Sum_of_no(int(n/10))

print(Sum_of_no(n))
print(1%10)