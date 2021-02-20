import sys
sys.stdin = open("./Input_Data/D3/6692.txt","r")

for T in range(int(input())):
    n = int(input())
    res = 0
    for i in range(n):
        a,b=map(float,input().split())
        res+=a*b
    print("#{} {:.6f}".format(T+1, res))