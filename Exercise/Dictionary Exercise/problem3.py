'''
Question 3
Create a dictionary to represent the open, high, low, close share price data 
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''

companies=['Python DS', 'PythonSoft', 'Pythazon','Pybook']
keys=['open', 'high', 'low', 'close']

prices = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]
d1={}

for i in range(len(keys)):
    d1[companies[i]]=dict(zip(keys,prices[i]))

print(d1)

