n=int(input('Please Enter a Positive integer: '))
def factorial(n):
    assert n>=0 and int (n)==n, "Sorry,but please enter only a positive integer"
    if n in [1,0]:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(n))