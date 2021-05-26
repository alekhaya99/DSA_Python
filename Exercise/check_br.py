def balanced_brackets(s):
    stacks=[]
    brackets={'(':')','{':'}','[':']'}
    for char in s:
        if char in brackets.keys():
            stacks.append(char)
        else:
            if len(stacks)==0 or brackets[stacks.pop()]!=char:
                return False
    return len(stacks)==0

s="[{()}]"

print(balanced_brackets(s))
