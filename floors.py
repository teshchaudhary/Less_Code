for _ in range(int(input())):
    X,Y=map(int,input().split())
    if  X%10==0 and Y%10==0:
        print(abs((X//10)-(Y//10)))
        
    elif X%10!=0 and Y%10==0:
        print(abs(((X//10)+1)-(Y//10)))
        
    elif X%10==0 and Y%10!=0:
        print(abs((X//10)-((Y//10)+1)))
        
    else:
        print(abs(((X//10)+1)-((Y//10)+1)))