n=int(input("Please Enter a number: "))

def sum(n):
    assert n>=0 and int(n)==n, "Please Enter a positive number"
    if n in [0]:
        return n
    else:
        return n+sum(n-1)

print(sum(n))