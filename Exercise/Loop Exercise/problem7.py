'''
Print
*****
*
***
*
*
*
'''

star='*'

for i in range(0,6):
    if i==0:
        for j in range(0,5):
            print(star, end='')
            if j==4:
                print()
    elif i==2:
        for j in range(3):
            print(star,end='')
            if j==2:
                print()
    else:
        print(star)
