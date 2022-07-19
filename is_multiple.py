def is_multiple(n,m):
    if n%m:
        return True
    else:
        return False

n,m=map(int,input().split())
print(is_multiple(n,m))