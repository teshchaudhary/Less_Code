for _ in range(int(input())):
    N,K=map(int,input().split())
    
    if N%5!=0:
        c=int(N/5)+1
    else:
        c=int(N/5)
        
    if K%5!=0:
        gr=int(K/5)+1
    else:
        gr=int(K/5)
        
    print(c-gr)