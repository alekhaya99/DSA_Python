letter=input("Please Enter a String")
length_letter=len(letter)

def Reverse_string(letter):
    if len(letter)==0:
        return letter
    else:
        return Reverse_string(letter[1:])+letter[0]

print(Reverse_string(letter))