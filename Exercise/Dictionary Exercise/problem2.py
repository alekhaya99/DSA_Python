'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence 
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}    
'''

n=int(input("Please enter a number"))
dict_fib={}

a = 0 
b = 1
d = dict()
for i in range(1,n+1):
   d[i] = a
   a,b = b,a+b
print(d)  

print(dict_fib)
