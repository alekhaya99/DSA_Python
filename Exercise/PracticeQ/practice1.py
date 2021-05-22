alphabet = 'abcdefghijklmnopqrstuvwxyz'
input_text=input("Please enter a word: ")

def shift_amount(i):
    return i%26

def encrypt(input_text,required_shift):
    out_string = ''
    input_text = input_text.lower()
    for char in input_text:
        if char not in alphabet:
            out_string = out_string + char
        else:    
            alpha_index = alphabet.find(char)
            out_string = out_string + alphabet[shift_amount(alpha_index +required_shift)]
    return out_string
