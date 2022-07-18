for _ in range(int(input())):
    N=int(input())
    S=input()
    res=""
    for i in range(0,N):
        if S[i]=="A":
            res+="T"
        elif S[i]=="T":
            res+="A"
        elif S[i]=="C":
            res+="G"
        elif S[i]=="G":
            res+="C"
    
    print(res)