import sys
sys.stdin = open("./Input_Data/D3/10505.txt","r")

for T in range(int(input())):
    n = int(input())
    l = list(map(int,input().strip().split()))
    cnt=0
    for i in range(n):
        if sum(l) / n >= l[i]:
            cnt+=1
    print("#{} {}".format(T+1, cnt))