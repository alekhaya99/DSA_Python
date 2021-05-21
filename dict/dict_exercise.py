import matplotlib.pyplot as plt
'''
Print an dictionary with the count of n_number of elements
'''

sentensce='''

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

'''

letter_count={}
for letter in sentensce:
    letter_count[letter.lower()]=letter_count.get(letter,0)+1

print(letter_count)



x,y=zip(*letter_count.items())
plt.bar(x,y)
plt.show()
letter_count_clean={}

for k,v in letter_count.items():
    if k.isalpha:
        letter_count_clean[k]=v

print(letter_count_clean)

x,y=zip(*letter_count_clean.items())
plt.bar(x,y)
plt.show()
