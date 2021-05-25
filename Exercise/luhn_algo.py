num=input("Please enter a nine digit number: ")
num_list=[int(i) for i in num]
num_list_reverse=num_list[::-1]
double=0
single=0
for i in range (0,len(num_list)):
    if i%2!=0:
        if num_list_reverse[i]>9:
            double=double+2*num_list_reverse[i]-9
        else:
            double=double+2*num_list_reverse[i]
    else:
        single=single+num_list_reverse[i]

if (double+single)%10==0:
    print(f'The card {num} is valid')
else:
    print(f'The card of {num} is not valid')
    