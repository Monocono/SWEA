import sys
sys.stdin = open('./Input_Data/D4/1226.txt','r')

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dfs(x,y):
    global res
    visit[x][y] = 1

    if map_list[x][y] == '3':
        res = 1
        return res
    
    for i in range(4):
        if 0<= x+dx[i] <N and 0<= y+dy[i]< N:
            if map_list[x+dx[i]][y+dy[i]] != '1' and visit[x+dx[i]][y+dy[i]] == 0:
                dfs(x+dx[i],y+dy[i])
    return res

for _ in range(10):
    T = int(input())
    N = 16
    map_list=[list(input()) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    res = 0

    for x in range(N):
        for y in range(N):
            if map_list[x][y] == '2':
                start_x = x
                start_y = y
                break
    print("#{} {}".format(T,dfs(start_x, start_y)))