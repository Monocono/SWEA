import sys
sys.stdin = open("./Input_Data/D3/2814.txt","r")

def dfs(idx,ans):
    global res
    visit[idx] = 0 
    ans += 1
    if res < ans: res = ans
    for i in graph[idx]:
        if visit[i]: dfs(i,ans)
    visit[idx] = 1

for T in range(int(input())):
    n,m = map(int,input().split())
    visit = [1 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    res = 0 
    for i in range(m):
        a,b= map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(n):
        dfs(i,0)
    print("#{} {}".format(T+1, res))