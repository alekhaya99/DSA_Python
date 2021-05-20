'''
Get the number and print the mean of that number

'''
your_input=input("Please enter a number: ")
numbers=[]

while your_input.lower() !="exit":
    while not your_input.isdigit():
        your_input=input("Do not enter string, enter only numbers: ")
    numbers.append(int(your_input))
    your_input=input("Please enter the next number: ")

total=0
for i in numbers:
    total+=i
print(f'The mean is {total/len(your_input)}')
