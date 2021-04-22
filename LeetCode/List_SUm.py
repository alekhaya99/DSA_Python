n=int(input("Please Enter the range of the two list"))
num_list1=[]
num_list2=[]

for i in range(n):
    number=int(input("Please Enter the {} number: ".format(i+1)))
    num_list1.append(number)


for j in range(n):
    number=int(input("Please Enter the {} number: ".format(j+1)))
    num_list2.append(number)

num_list1.reverse()
num_list2.reverse()
strings = [str(integer) for integer in num_list1]
a_string = "".join(strings)
a= int(a_string)
strings = [str(integer) for integer in num_list2]
a_string = "".join(strings)
b= int(a_string)
# a=num_list1_updated.join()
# b=num_list2_updated.join()
print(a)
print(b)
c=a+b
print(c)

result=list(map(int,str(c)))
result.reverse()

print(result)
