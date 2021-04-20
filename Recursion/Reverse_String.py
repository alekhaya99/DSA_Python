letter=input("Please Enter a String: ")
length_letter=len(letter)

def Reverse_string(letter):
    if len(letter)==0:
        return letter
    else:
        return Reverse_string(letter[1:])+letter[0]

def Reverse_string_itteration(letter):
    updated_letter=""
    for i in range(-1,-length_letter-1,-1):
        updated_letter=updated_letter+letter[i]
    return updated_letter

print(Reverse_string(letter))
print(Reverse_string_itteration(letter))