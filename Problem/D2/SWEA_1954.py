import sys
sys.stdin = open("./Input_Data/D2/1954.txt", "r")

for T in range(int(input())):
    n=int(input())
    res = [[0]*n for a in range(n)]
    dx=[0,1,0,-1]; dy=[1,0,-1,0]
    option=x=y=0
    res[x][y]=1

    for i in range(2,n**2+1):
        x+=dx[option]; y+=dy[option]
        res[x][y]=i
        if 0<= x+dx[option] <n and 0<=y+dy[option]<n and not res[x+dx[option]][y+dy[option]]:
            continue
        if option !=3:
            option+=1
        else:
            option = 0

    print("#{}".format(T+1))
    for _ in res:
        print(*_)