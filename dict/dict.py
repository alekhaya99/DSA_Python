capitals={'India':'New Delhi','Singapore':'Singapore','Australia':'Canberra'}

#In order to get the value of dictionary
print(capitals['India'])
print(capitals.get('India'))

#Add value to a dictionary
capitals['Germany']='Berlin'

print(capitals.items())

for country,city in capitals.items():
    print(f'The capital of {country} is {city}')


if 'Singapore' in capitals:
    print('SG is there')