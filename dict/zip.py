list1=[1,2,3,4]
list2=['A','B','C','D']

joined=list(zip(list1,list2))

print(joined)

i,j=zip(*joined)