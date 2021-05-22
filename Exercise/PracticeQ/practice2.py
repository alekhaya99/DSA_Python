def match_sum(input_variable,target_variable):
    dict1={}
    for i in range(len(input_variable)):
        if target_variable-input_variable[i] in dict1:
            print(dict1)
            return [dict1[target_variable-input_variable[i]],i]
        dict1[input_variable[i]]=i
    return -1

print(match_sum([1,4,7,9],13))
