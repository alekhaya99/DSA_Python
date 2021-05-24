
def check_sum(list1,num):
    dict1={}
    for i in range(len(list1)):
        if num-list1[i] in dict1:
            print(dict1)
            return [dict1[num-list1[i]],i]
        dict1[list1[i]]=i
    return -1

print(check_sum([1,2,4,5,7],9))
