Arr=int(input("Enter the length of the list"))
List1=[]
for i in range(Arr):
    List=int(input("Enter number "))
    List1.append(List)
# Array=[111,3,4,7,234,89]
n=len(List1)
def Greatest_no(List1,n):
    if n==1:
        return List1[0]
    return max(List1[n-1],Greatest_no(List1,n-1))

# print(Greatest_no(Array,n))
print(Greatest_no(List1,Arr))


def Greatest_no_recursionless(List1):
    Demo_no=List1[0]
    for index in range(0,n):
        if List1[index]>Demo_no:
            Demo_no=List1[index]
    return Demo_no

print(Greatest_no_recursionless(List1))


