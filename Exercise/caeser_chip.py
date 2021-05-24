alphabet = 'abcdefghijklmnopqrstuvwxyz'
input_text=input("Please enter the text: ")

n=int(input("Please enter the number: "))

def check_index(n):
    return n%26

def shift_alpha(input_text,n):
    modified_txt=""
    input_text=input_text.lower()
    for i in input_text:
        if i not in alphabet:
            modified_txt=modified_txt+i
        else:
            alpha_index=alphabet.find(i)
            modified_txt=modified_txt+alphabet[check_index(n+alpha_index)]
    return modified_txt

print(shift_alpha(input_text,n))