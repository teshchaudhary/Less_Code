import random as r
def chois(l):
    x=r.randrange(max(l)+1)
    if x in l:
        return x
    else:
        return chois(l)
l=list(map(int,input().split()))
print(chois(l))