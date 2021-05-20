length_of_list=int(input("Please Enter the length of the list"))
data=[]
for i in range(length_of_list):
    a=int(input(f'Please enter the {i} number: '))
    data.append(a)
print(f'The unsorted list is {data}')
data_copy=data[:]
for i in range(length_of_list):
    for j in range(0,length_of_list-i-1):
        if data_copy[j]>data_copy[j+1]:
            data_copy[j],data_copy[j+1]=data_copy[j+1],data_copy[j]

print(f'The sorted list is {data_copy}')