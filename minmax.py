from numpy import mask_indices


import random
def minmax(l):
    maks=l[0]
    meen=l[0]
    for i in range(len(l)):
        if l[i]>maks:
            maks=l[i]
        elif l[i]<meen:
            meen=l[i]
    return(maks,meen)

l=random.shuffle(list(range(10001)))
print(minmax(l))