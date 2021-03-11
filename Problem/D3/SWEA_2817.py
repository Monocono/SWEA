import sys
sys.stdin = open("./Input_Data/D3/2817.txt","r")

def solve(idx, sum):
    global res
    if idx >= n: return
    temp = sum + l[idx]
    if temp == k: res+=1
    solve(idx+1,temp)
    solve(idx+1,sum)
    
for T in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    res = 0
    solve(0,0)
    print("#{} {}".format(T+1,res))
