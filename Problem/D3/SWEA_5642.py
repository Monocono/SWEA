import sys
sys.stdin = open("./Input_Data/D3/5642.txt","r")

for T in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    m = temp = 0
    for i in range(n):
        temp = temp + l[i]
        if temp < 0: temp = 0
        elif temp > m: m = temp
    if max(l) < 0: m = max(l)
    print("#{} {}".format(T+1, m))