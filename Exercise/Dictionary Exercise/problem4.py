'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should 
be random numbers created from the random module. Can you draw a bar graph of 
the results?
'''

import random

keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d=dict()

for i in (keys):
    d[i]=random.randint(1,100)

print(d)
