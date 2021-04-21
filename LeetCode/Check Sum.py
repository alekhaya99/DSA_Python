num_list=int(input("Please enter the size of the list: "))

my_list=[]
for i in range(num_list):
    number=int(input("Please Enter the {} number: ".format(i+1)))
    my_list.append(number)

print(my_list)

checked_number=int(input("Please enter the sum of the number you want to check "))

def search_numbers(my_list):
    sum_list=[]
    for i in range(num_list):
        for j in range(num_list):
            if i!=j:
                sum_of_list=my_list[i]+my_list[j]
                if sum_of_list==checked_number:
                    sum_list.append(i)
                    sum_list.append(j)
                    return sum_list
                   
    if sum_list==[]:
        a="there are no match"
        return(a)
           
print(search_numbers(my_list))

                
