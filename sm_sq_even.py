def sm(l):
    if l==[]:
        return 0
    else:
        return l[0]+sm(l[1:])

l=[i**2 for i in range(int(input())+1) if i%2==0]
print(sm(l))