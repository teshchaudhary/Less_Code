def wordle(s1,s2):
    s=""
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            s+="G"
        else:
            s+="B"
    return(s)

s1,s2=map(str,input().split())
print(wordle(s1,s2))