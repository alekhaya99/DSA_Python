with open('hello.txt','r') as f:
    for line in f.readlines():
        print(line,end='')