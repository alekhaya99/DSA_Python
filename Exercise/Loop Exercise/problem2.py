'''
Question2:
Ask an user to enter a sting and enter in reverse order
'''
Str_word=input("Please enter a word: ")
Str_word=str(Str_word)

reverse_word=''
for i in Str_word:
    reverse_word=i+reverse_word

print(reverse_word)