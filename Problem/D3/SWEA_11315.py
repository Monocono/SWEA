# not solve
import sys
sys.stdin = open("./Input_Data/D3/11315.txt","r")

dir_x=[0,1,1,1]
dir_y=[1,1,0,-1]
def dfs(x,y,cnt):
    global flag
    if cnt >= 5:
        flag = 1
        return
    for i in range(n):
        if 0<=x+dir_x[i]< n and 0<=y+dir_y[i]< n:
            if l[x+dir_x[i]][y+dir_y[i]] == 'o':
                dfs(x+dir_x[i],y+dir_y[i],cnt+1)
    return

for T in range(int(input())):
    
    n = int(input())
    l = [list(map(str,input())) for x in range(n)]

    flag = 0
    for a in range(n):
        if flag == 1: break
        for b in range(n):
            if flag == 1: break
            if l[a][b] == 'o':
                dfs(a,b,0)
                if flag == 1: break
    
    print("#{} {}".format(T+1, "YES" if flag == 1 else "NO"))