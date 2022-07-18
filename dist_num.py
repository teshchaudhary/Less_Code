def dist_num(l):
    c=0
    x=sorted(l)
    for i in range(len(l)):
        if x[i-1]!=x[i]:
            c+=1
    return c

l=list(map(int,input().split()))
print(dist_num(l))