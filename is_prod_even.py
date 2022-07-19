# Checks which pairs of consecutive numbers in the list can give a even mutiple

def is_prod_even(l):
    ev_lis=[]
    for i in range(1,len(l)):
        if l[i-1]*l[i]%2==0:
            ev_lis.append((l[i-1],l[i]))
        elif i+1==len(l) and l[i-1]*l[i]%2!=0:
            return False
    return ev_lis
l=list(map(int,input().split()))
print(is_prod_even(l))