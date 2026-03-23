def hanoi_tower(n,fr,tmp,to) : # 출발기둥 from , 임시기둥 tmp, 목적기둥 to
    if(n==1):
        print("원반 1: %s -> %s" %(fr,to))
    else:
        hanoi_tower(n-1, fr,to,tmp)
        print("원반 %d: %s -> %s" %(n,fr,to))
        hanoi_tower(n-1, tmp, fr,to)



hanoi_tower(4,'A','B','C')

def sub(n):
    if n <= 1:
        return n
    return sub(n-1) + sub(n-2)

print(sub(3))

def asterisk(i):
    if i > 1:
        asterisk(i/2)
        asterisk(i/2)
    print("*", end="")
asterisk(5)