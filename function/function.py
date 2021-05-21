def calculate_mean(first,*remainder):
    mean=(first+sum(remainder))/(len(remainder)+1)
    return mean

print(calculate_mean(2,2,2,2,2))