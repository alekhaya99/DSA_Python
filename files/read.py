f=open('hello.txt','r')

print(f.read())

# //Gives the first line of the file//
print(f.readline())
# //Gives all the lines line of the file//
print(f.readlines())
f.close()