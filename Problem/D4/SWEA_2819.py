import sys
sys.stdin = open("./Input_Data/D4/2819.txt", "r")

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(x,y,s):
    s+=l[x][y]
    if len(s) == 7:
        res.add(s)
        return
    for i in range(4):
        if 0<= x +dx[i] <4 and 0<= y+dy[i]<4:
            dfs(x+dx[i],y+dy[i],s)

for T in range(int(input())):
    l =[list(map(str,input().split())) for _ in range(4)]
    res = set(); res.clear()
    for x in range(4):
        for y in range(4):
            dfs(x,y,"")
    print("#{} {}".format(T+1, len(res)))
