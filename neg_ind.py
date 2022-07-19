def neg_in(S,Ch):
    for i in range(len(S)):
        if S[i]==Ch:
            return(i-len(S))

S,Ch=map(str,input().split()[:2])
print(neg_in(S,Ch))