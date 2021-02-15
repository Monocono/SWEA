import sys
sys.stdin = open("./Input_Data/D3/5431.txt","r")

for T in range(int(input())):
    n,k = map(int,input().strip().split())
    k_l = list(map(int,input().split()))
    res = []
    for per in range(1,n+1):
        if per not in k_l:
            res.append(per)
    print("#{}".format(T+1), *res)
