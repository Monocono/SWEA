import sys
sys.stdin = open("./Input_Data/D3/1216.txt","r")

# 가존코드 시간이 너무 오래걸림
for T in range(10):
    n = 100
    k, res = 1,1
    tc = int(input())
    rl = [list(map(str,input())) for _ in range(n)]
    cl = list(map(list,zip(*rl)))
    flag = False
    for a in range(100):
        flag = False
        for b in range(100):
            for c in range(101-k):
                row = rl[b][c:c+k]
                col = cl[b][c:c+k]
                if row == row[::-1] or col == col[::-1]:
                    res = k
                    flag = True
                    break
            if flag:
                break
        k +=1
    print("#{} {}".format(tc, res))

#수정코드 시간 단축
def solve(l,n,k):
    for a in range(n):
        for b in range(n-k+1):
            for c in range(k//2):
                if l[a][b+c] != l[a][b+k-1-c]:
                    break
            else:
                    return k
    return 0

for T in range(10):
    n= 100
    m=int(input())
    l=[list(map(str,input())) for _ in range(n)]
    res = 1
    k = 2
    while k<=n and k <= res+2:
        if res < solve(l,n,k):  
            res = k
        k+=1
    k = res+1
    while k<=n and k <= res+2:
        if res < solve(list(zip(*l)),n,k):  
            res = k
        k+=1
    print("#{} {}".format(T+1, res))