n=int(input("Please Enter a number: "))

def Dec_Binary(n):
    assert n>=0 and int(n)==n, "Please Enter a positive integer"
    if n==0:
        return 0
    else:
        return (n%2)+10*Dec_Binary(int(n/2))

print(Dec_Binary(n))