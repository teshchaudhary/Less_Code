#Cannot use multiplication, modulo or division

#Naive Approach
def is_even(k):
    flg=True
    while flg:
        if k==2 or k==0:
            flg=False
            return True
        else:
            k-=2
            if k==2:
                return True
            elif k<0:
                return False

#Recursive Approach
def is_even_rec(k):
    if k==2 or k==0:
        return True
    elif k<0:
        return False
    else:
        return is_even_rec(k-2)

k=int(input())
print(is_even(k))